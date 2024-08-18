from tkinter import *
import tkinter.font as font
from tkinter import messagebox
import customtkinter
import subprocess
import webbrowser

class main:
    def __init__(self):
        self.root = Tk()
        self.root.title("BaitBox Honeypot")
        self.root.geometry('600x700+600+200')
        self.root.minsize(500, 300)
        self.root.maxsize(500, 300)
        self.root.configure(bg='Sky blue')
        self.root.iconbitmap("E:\Class\Semester 6\CyberSecurity Project\Final\Resources\icon.ico")
        self.f1 = font.Font(family='Serif', size='30')
        self.f2 = font.Font(family='Serif', size='10')
        self.f3 = font.Font(family='Serif', size='20')
        self.pic = PhotoImage(file='E:\Class\Semester 6\CyberSecurity Project\Final\Resources\honey.png')

        self.p1 = Label(self.root, image=self.pic)
        self.p1.pack()

        self.ssh_button = customtkinter.CTkButton(master=self.root,
                                                  text='SSH Service',
                                                  command=lambda: self.service("SSH"),
                                                  corner_radius=10,
                                                  bg_color=("#192235", "#192235"),
                                                  fg_color=("dodger blue", "dodger blue"))
        self.ssh_button.place(relx='0.1', rely='0.1')

        self.ftp_button = customtkinter.CTkButton(master=self.root,
                                                  text='FTP Service',
                                                  command=lambda: self.service("FTP"),
                                                  corner_radius=10,
                                                  bg_color=("#192235", "#192235"),
                                                  fg_color=("dodger blue", "dodger blue"))
        self.ftp_button.place(relx='0.1', rely='0.3')

        self.telnet_button = customtkinter.CTkButton(master=self.root,
                                                     text='Telnet Service',
                                                     command=lambda: self.service("Telnet"),
                                                     corner_radius=10,
                                                     bg_color=("#192235", "#192235"),
                                                     fg_color=("dodger blue", "dodger blue"))
        self.telnet_button.place(relx='0.1', rely='0.5')

        self.http_button = customtkinter.CTkButton(master=self.root,
                                                   text='HTTP Service',
                                                   command=lambda: self.service("HTTP"),
                                                   corner_radius=10,
                                                   bg_color=("#192235", "#192235"),
                                                   fg_color=("dodger blue", "dodger blue"))
        self.http_button.place(relx='0.1', rely='0.7')

        self.exit_button = customtkinter.CTkButton(master=self.root,
                                                   text='Exit',
                                                   command=self.root.quit,
                                                   corner_radius=10,
                                                   bg_color=("#192235", "#192235"),
                                                   fg_color=("dodger blue", "dodger blue"))
        self.exit_button.place(relx='0.7', rely='0.9')

        self.logs_button = customtkinter.CTkButton(master=self.root,
                                                   text='LOGS',
                                                   command=self.warning,
                                                   corner_radius=10,
                                                   bg_color=("#192235", "#192235"),
                                                   fg_color=("dodger blue", "dodger blue"))
        self.logs_button.place(relx='0.7', rely='0.5')

        self.root.mainloop()

    def logs_site(self):
        webbrowser.open("http://localhost:3000/d/fdr4ob64qknwgf/honeypot-logs?orgId=1")
        
    def warning(self):
        messagebox.showwarning("Caution!", "Please setup Grafana before viewing logs in web browser.")
        self.logs_site()

    def service(self, service_name):
        self.new_window = Toplevel()
        self.new_window.title(service_name + " Honeypot")
        self.new_window.geometry("500x300")
        self.new_window.minsize(500, 300)
        self.new_window.maxsize(500, 300)

        self.new_window.iconbitmap("E:\Class\Semester 6\CyberSecurity Project\Final\Resources\icon.ico")

        self.bg_label = Label(self.new_window, image=self.pic)
        self.bg_label.place(relwidth=1, relheight=1)

        self.label_font = ("Helvetica", 16, "bold")
        self.label_fg_color = ("white", "white")  # White text color for better contrast
        self.label_bg_color = "#182134"

        self.label_padding_x = 100

        self.host_label = customtkinter.CTkLabel(self.new_window, 
                                                text="Host IP Address", 
                                                font=self.label_font, 
                                                text_color=self.label_fg_color,
                                                fg_color=self.label_bg_color,
                                                bg_color=("#192235", "#192235"))
        self.host_label.pack(pady=5, padx=(self.label_padding_x, 0), anchor="w")
        self.host_entry = customtkinter.CTkEntry(self.new_window,
                                                bg_color=("#192235", "#192235"))
        self.host_entry.insert(0, "127.0.0.1")
        self.host_entry.pack(pady=5, padx=(self.label_padding_x, 0), anchor="w")

        self.port_label = customtkinter.CTkLabel(self.new_window, 
                                                text="Port", 
                                                font=self.label_font, 
                                                text_color=self.label_fg_color,
                                                fg_color=self.label_bg_color,
                                                bg_color=("#192235", "#192235"))
        self.port_label.pack(pady=5, padx=(self.label_padding_x, 0), anchor="w")
        self.port_entry = customtkinter.CTkEntry(self.new_window,
                                                bg_color=("#192235", "#192235"))
        self.port_entry.insert(0, "2222")
        self.port_entry.pack(pady=5, padx=(self.label_padding_x, 0), anchor="w")

        if service_name == "HTTP":
            self.url_label = customtkinter.CTkLabel(self.new_window, 
                                                    text="URL", 
                                                    font=self.label_font, 
                                                    text_color=self.label_fg_color,
                                                    fg_color=self.label_bg_color,
                                                    bg_color=("#192235", "#192235"))
            self.url_label.pack(pady=5, padx=(self.label_padding_x, 0), anchor="w")
            self.url_entry = customtkinter.CTkEntry(self.new_window,
                                                    bg_color=("#192235", "#192235"))
            self.url_entry.insert(0, "http://example.com")
            self.url_entry.pack(pady=5, padx=(self.label_padding_x, 0), anchor="w")

        self.btn_start = customtkinter.CTkButton(master=self.new_window,
                                                 text=f'Start Honeypot {service_name}',
                                                 command=lambda: self.honeypot_start(service_name),
                                                 corner_radius=10,
                                                 bg_color=("#192235", "#192235"),
                                                 fg_color=("dodger blue", "dodger blue"))
        self.btn_start.place(relx='0.2', rely='0.82')

        self.btn_quit = customtkinter.CTkButton(master=self.new_window,
                                                command=self.stop_honeypot,
                                                corner_radius=10,
                                                bg_color=("#192235", "#192235"),
                                                text='Quit',
                                                fg_color=("dodger blue", "dodger blue"))
        self.btn_quit.place(relx='0.63', rely='0.82')


    def honeypot_start(self, service_name):
        host = self.host_entry.get()
        port = self.port_entry.get()

        if service_name == "HTTP":
            url = self.url_entry.get().strip()
        else:
            url = None

        try:
            port = int(port)
            if service_name == "SSH":
                self.honeypot_process = subprocess.Popen(["python", "ssh.py", host, str(port)])
                messagebox.showinfo("Success", "SSH Honeypot Server Started")
            elif service_name == "FTP":
                self.honeypot_process = subprocess.Popen(["python", "ftp.py", host, str(port)])
                messagebox.showinfo("Success", "FTP Honeypot Server Started")
            elif service_name == "Telnet":
                self.honeypot_process = subprocess.Popen(["python", "telnet.py", host, str(port)])
                messagebox.showinfo("Success", "Telnet Honeypot Server Started")
            elif service_name == "HTTP":
                self.honeypot_process = subprocess.Popen(["python", "http_honeypot.py", host, str(port), url])
                messagebox.showinfo("Success", "HTTP Honeypot Server Started")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid port number.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start {service_name} Honeypot Server: {e}")

    def stop_honeypot(self):
        if self.honeypot_process:
            self.honeypot_process.terminate()  # Send termination signal
            try:
                self.honeypot_process.wait(timeout=5)  # Wait for the process to terminate
            except subprocess.TimeoutExpired:
                self.honeypot_process.kill()  # Forcefully kill if terminate doesn't work
            finally:
                self.honeypot_process = None
                messagebox.showinfo("Stopped", "Honeypot Server Stopped.")
        self.new_window.destroy()


if __name__ == "__main__":
    main()



