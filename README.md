# Network Port Scanner & Risk Analyzer

A Python-based network security tool that scans a target IP address or domain to identify open TCP ports, detect running services, and analyze potential security risks.  
The tool generates a detailed security report for each scan.

 This project is intended for **educational and authorized security testing only**.

---

## Project Overview

Open network ports often act as entry points for cyber attacks.  
This project helps in basic **network reconnaissance and risk assessment** by:

- Scanning commonly used network ports
- Identifying services running on open ports
- Categorizing ports based on security risk
- Providing descriptive risk explanations
- Generating audit-style scan reports

---

## Features

- Scan **top common TCP ports**
- Detect open ports using TCP connect scanning
- Identify services based on port numbers
- Categorize risk as **High / Medium / Low**
- Provide detailed **risk descriptions**
- Display results in CLI
- Generate uniquely named **TXT reports**
- Works on **Windows & Linux (Kali)**

---

## Technologies Used

| Component | Technology |
|--------|------------|
| Language | Python 3 |
| Networking | socket (TCP) |
| OS | Windows / Linux |
| Dependencies | None (Standard Library Only) |

---

## Risk Classification Logic

| Risk Level | Description |
|----------|-------------|
| High | Remote access services, databases, admin interfaces, clear-text protocols |
| Medium | Web services, email services, information disclosure risks |
| Low | Encrypted and secured services |

Each detected open port is accompanied by a **clear explanation of its security impact**.

---

## Project Structure

# Network Port Scanner

network-port-scanner/
│
├── main.py                  # Main execution entry point
│
├── scanner.py               # TCP port scanning engine
│
├── services.py              # Port number to service mapping
│
├── risk.py                  # Risk classification and vulnerability descriptions
│
├── report.py                # Scan result report generation
│
├── requirements.txt         # Required Python dependencies
│
└── README.md                # Project documentation

---

## How to Run the Project

### On Windows
>python main.py

### On Linux / Kali
>python3 main.py

Enter a target IP or domain when prompted.

## Safe Test Targets
127.0.0.1
scanme.nmap.org
example.com
Your device IP

## Output

Console output showing open ports, services, and risks

Automatically generated report file:

scan_report_<target>_<timestamp>.txt
