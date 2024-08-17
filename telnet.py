import os
import sys
import argparse
from twisted.python import log
from twisted.logger import textFileLogObserver
from twisted.protocols import basic
from twisted.internet import reactor, protocol, endpoints

script_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = script_dir + "\Logs"

class SimpleTelnetProtocol(basic.LineReceiver):
    delimiter = b"\n"
    maxAttempts = 3

    def __init__(self):
        self.attempts = 0
        self.expectingPassword = False

    def connectionMade(self):
        client_ip = self.transport.getPeer().host
        client_port = self.transport.getPeer().port
        log.msg(f"TELNET NEW Connection - Client IP: {client_ip}, Port: {client_port}")
        self.transport.write(b"Welcome to the Telnet Honeypot!\r\n")
        self.promptForUsername()

    def promptForUsername(self):
        self.expectingPassword = False
        self.transport.write(b"Username: ")

    def promptForPassword(self):
        self.expectingPassword = True
        self.transport.write(b"Password: ")

    def lineReceived(self, line):
        if self.expectingPassword:
            log.msg(f"Received password attempt: {line}")
            self.attempts += 1
            if self.attempts < self.maxAttempts:
                self.transport.write(b"Wrong password.\r\n")
                self.promptForUsername()
            else:
                log.msg("Maximum attempts reached. Disconnecting client.")
                self.transport.write(b"Too many wrong attempts. Disconnecting.\r\n")
                self.transport.loseConnection()
        else:
            log.msg(f"Received username attempt: {line}")
            self.promptForPassword()

    def connectionLost(self, reason):
        log.msg("Connection lost")


class SimpleTelnetFactory(protocol.ServerFactory):
    protocol = SimpleTelnetProtocol


def setup_telnet_honeypot(host, port):
    LOG_FILE_PATH = os.path.join(log_dir, "telnet_honeypot.log")
    print(f"TELNET HONEYPOT ACTIVE ON HOST: {host}, PORT: {port}")
    print(f"ALL attempts will be logged in: {LOG_FILE_PATH}")

    log_observer = textFileLogObserver(open(LOG_FILE_PATH, "a"))
    log.startLoggingWithObserver(log_observer, setStdout=False)

    telnet_factory = SimpleTelnetFactory()

    endpoint = endpoints.TCP4ServerEndpoint(reactor, port, interface=host)
    endpoint.listen(telnet_factory)
    reactor.run()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python telnet_honeypot.py <host> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])

    setup_telnet_honeypot(host, port)

