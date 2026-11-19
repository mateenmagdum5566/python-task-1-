# Basic Network Sniffer

A beginner-friendly Python project that captures network packets and displays useful packet **metadata**.

## Features

- Captures a chosen number of packets.
- Displays timestamp, source IP, destination IP and protocol.
- Shows TCP/UDP source and destination ports when available.
- Shows packet size in bytes.
- Supports IPv4, IPv6 and ARP packets.
- Does not display packet payload contents, helping avoid exposure of private data.

## Requirements

- Python 3.9 or newer
- Scapy
- Packet-capture support on your operating system

## Installation

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows:

   ```bash
   .venv\Scripts\activate
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

4. Install the dependency:

   ```bash
   pip install -r requirements.txt
   ```

### Operating-system notes

- **Windows:** Install Npcap from its official website. Run the terminal with the permissions required by Npcap.
- **Linux:** Packet capture may require elevated privileges or suitable capture capabilities.
- **macOS:** Packet capture may require administrator privileges.

## Run the program

Capture 20 packets:

```bash
python network_sniffer.py
```

Capture 50 packets:

```bash
python network_sniffer.py --count 50
```

Choose a network interface:

```bash
python network_sniffer.py --count 20 --interface "INTERFACE_NAME"
```

Replace `INTERFACE_NAME` with an interface available on your computer. You can check available interfaces in Python with:

```python
from scapy.all import get_if_list
print(get_if_list())
```

## Example output

The values below are illustrative sample data, not a live capture.

```text
BASIC NETWORK SNIFFER
Capturing packet metadata only. Payload contents are not displayed.

TIME     | PROTOCOL       | SOURCE                                  | DESTINATION                             | PORTS              | SIZE
12:30:01 | TCP            | 192.168.1.10                            | 93.184.216.34                           | 51520 -> 443       | 74 bytes
12:30:02 | UDP            | 192.168.1.10                            | 192.168.1.1                             | 53000 -> 53        | 70 bytes
12:30:03 | ICMP           | 192.168.1.1                             | 192.168.1.10                            | -                  | 98 bytes
```

## How it works

1. Scapy listens for packets on the selected interface.
2. Each captured packet is checked for common protocol layers.
3. The program reads available IP addresses and TCP/UDP ports.
4. It calculates the packet size and prints a formatted summary.
5. `store=False` avoids keeping the captured packets in memory.

## Project structure

```text
basic-network-sniffer/
├── network_sniffer.py
├── requirements.txt
└── README.md
```

## Learning outcomes

- Basic packet capture with Python and Scapy.
- Understanding source and destination addresses.
- Recognizing TCP, UDP, ICMP, IPv6 and ARP.
- Understanding ports and packet sizes.
- Learning how network traffic is observed.

## Safety and privacy

Use this program only on your own device/network or where you have explicit permission. Do not monitor other people's traffic. This project displays packet metadata only and intentionally avoids printing payload contents, passwords, messages or other private data.
