# PRODIGY_CS_05 - Network Packet Analyzer

## Objective
Develop a packet sniffer that captures and analyzes network packets to understand network traffic and packet structures.

## Description
This project is a simple Network Packet Analyzer built using Python and the Scapy library. It captures live network packets and displays useful information such as source IP address, destination IP address, protocol type, and packet summary.

## Features
- Captures live network packets
- Displays source and destination IP addresses
- Identifies protocol information
- Shows packet summaries
- Helps understand network communication

## Technologies Used
- Python
- Scapy

## Installation

Install the required library:

```bash
pip install scapy
```

## Usage

Run the script:

```bash
python packet_analyzer.py
```

The program will capture packets and display their details in the terminal.

## Sample Output

```text
--- Packet Captured ---
Source IP: 192.168.1.5
Destination IP: 142.250.183.78
Protocol: 6
IP / TCP 192.168.1.5:51234 > 142.250.183.78:https
```

## Project Structure

PRODIGY_CS_05/
│
├── packet_analyzer.py
├── output.txt
└── README.md

## Learning Outcomes
- Understanding packet structures
- Network traffic analysis
- Working with Python networking libraries
- Basic cybersecurity concepts

## Author
Siya Shinde
