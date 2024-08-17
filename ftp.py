import os
import argparse
from twisted.internet import reactor, protocol, endpoints
from twisted.protocols import basic
from twisted.logger import textFileLogObserver
from twisted.python import log
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = script_dir + "\Logs"

class SimpleFTPProtocol(basic.LineReceiver):
    delimiter = b"\r\n"
    maxAttempts = 3

    def __init__(self):
        self.attempts = 0
        self.userReceived = False

    def connectionMade(self):
        client_ip = self.transport.getPeer().host
        client_port = self.transport.getPeer().port
        log.msg(f"FTP NEW Connection - Client IP: {client_ip}, Port: {client_port}")
        self.sendLine(b"220 Welcome to the FTP Honeypot")

    def lineReceived(self, line):
        log.msg(f"Received data: {line}")

        line_str = line.decode("utf-8")
        command = line_str.split(" ")[0].upper()

        if command == "USER":
            self.userReceived = True
            self.sendLine(b"331 Username okay, need password")
        elif command == "PASS" and self.userReceived:
            self.attempts += 1
            if self.attempts < self.maxAttempts:
                self.sendLine(b"530 Login incorrect")
                self.userReceived = False
            else:
                log.msg("Maximum attempts reached. Disconnecting client.")
                self.sendLine(b"530 Too many wrong attempts. Disconnecting.")
                self.transport.loseConnection()
        else:
            self.sendLine(b"500 Syntax error, command unrecognized")

    def sendLine(self, line):
        self.transport.write(line + self.delimiter)

    def connectionLost(self, reason):
        log.msg("Connection lost")


class SimpleFTPFactory(protocol.ServerFactory):
    protocol = SimpleFTPProtocol


def setup_ftp_honeypot(host, port):
    LOG_FILE_PATH = os.path.join(log_dir, "ftp_honeypot.log")
    print(f"FTP HONEYPOT ACTIVE ON HOST: {host}, PORT: {port}")
    print(f"ALL attempts will be logged in: {LOG_FILE_PATH}")

    log_observer = textFileLogObserver(open(LOG_FILE_PATH, "a"))
    log.startLoggingWithObserver(log_observer, setStdout=False)

    ftp_factory = SimpleFTPFactory()

    endpoint = endpoints.TCP4ServerEndpoint(reactor, port, interface=host)
    endpoint.listen(ftp_factory)
    reactor.run()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ftp_honeypot.py <host> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])

    setup_ftp_honeypot(host, port)