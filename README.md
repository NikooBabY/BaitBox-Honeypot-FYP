# BaitBox: A Multi-Service Low-Interaction Honeypot

#Sulavkarki
#210350
#Softwarica College of IT and E-Commerce
#Final Year Project
#2024

## Overview
BaitBox is a multi-service low-interaction honeypot designed to enhance cybersecurity for commercial banks in the Kathmandu Valley. It emulates various network services, including SSH, FTP, Telnet, and HTTP, to attract, log, and analyze unauthorized access attempts. The honeypot provides a proactive approach to security, allowing organizations to detect and study attack patterns in a controlled environment.

## Features
- **Multi-Service Emulation**: Supports SSH, FTP, Telnet, and HTTP protocols.
- **Logging and Alerting**: Captures and logs all access attempts, with logs visualized using Grafana.
- **Realistic Service Interaction**: Simulates login prompts and basic interactions to engage attackers.
- **Custom GUI**: Developed using `tkinter` and `customtkinter` for easy management of honeypot services.
- **Proactive Security**: Provides insights into potential threats, helping to enhance overall network security.

## Frontend
- **GUI**: The honeypot is managed through a graphical user interface developed using `tkinter` and `customtkinter`. The GUI allows users to start, stop, and monitor different honeypot services, with real-time status updates and easy navigation.

## Backend
- **Emulated Services**: Python scripts are used to emulate SSH, FTP, Telnet, and HTTP services. These services mimic real-world interactions, attracting potential attackers while logging their activities.
- **Logging Mechanism**: Logs are stored in text files, which are later visualized using Grafana for better analysis and alerting.
- **Web Scraper and Crawler**: Used for the HTTP service to fetch and serve a real website, making the honeypot more convincing.

## Tools and Technologies
- **Python**: Core programming language used for developing the honeypot.
- **tkinter and customtkinter**: Used for building the graphical user interface.
- **Twisted Framework**: Powers the network services, handling connections and data processing.
- **BeautifulSoup**: Used for web scraping to support the HTTP emulation.
- **Grafana**: Visualizes the logs and helps set up alerts for suspicious activities.

## Limitations
1. **Limited Interaction**: Only supports basic interaction, limiting the capture of advanced attack behaviors.
2. **Resource Intensive**: Requires significant system resources to run multiple services.
3. **Static Emulation**: Fixed service responses may be less effective against sophisticated attackers.
4. **Single-Environment Focus**: Designed for specific protocols and environments.
5. **Dependency on External Tools**: Relies on external tools like Grafana for log visualization and alerting.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/BaitBox.git
2. Navigae to Project directory:
   ```bash
   cd BaitBox
3. Update the paths in GUI 
4. Installed Python Packages required
5. Run the Main.py
