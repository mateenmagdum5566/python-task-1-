"""
Basic Network Sniffer
Captures packet metadata on a network you own or are authorized to monitor.

This beginner project displays timestamp, source/destination IPs, protocol,
ports (when available), and packet size. It intentionally does not print
packet payloads, which may contain private information.
"""

import argparse
from datetime import datetime

from scapy.all import sniff, IP, IPv6, TCP, UDP, ICMP, ARP


def describe_packet(packet):
    """Return a short, privacy-conscious description of one packet."""
    timestamp = datetime.now().strftime("%H:%M:%S")

    if IP in packet:
        source = packet[IP].src
        destination = packet[IP].dst
    elif IPv6 in packet:
        source = packet[IPv6].src
        destination = packet[IPv6].dst
    elif ARP in packet:
        source = packet[ARP].psrc
        destination = packet[ARP].pdst
    else:
        source = "N/A"
        destination = "N/A"

    if TCP in packet:
        protocol = "TCP"
        ports = f"{packet[TCP].sport} -> {packet[TCP].dport}"
    elif UDP in packet:
        protocol = "UDP"
        ports = f"{packet[UDP].sport} -> {packet[UDP].dport}"
    elif ICMP in packet:
        protocol = "ICMP"
        ports = "-"
    elif ARP in packet:
        protocol = "ARP"
        ports = "-"
    elif IPv6 in packet:
        protocol = "IPv6 (other)"
        ports = "-"
    elif IP in packet:
        protocol = f"IP protocol {packet[IP].proto}"
        ports = "-"
    else:
        protocol = "Other"
        ports = "-"

    size = len(packet)
    return (
        f"{timestamp} | {protocol:<14} | {source:<39} | "
        f"{destination:<39} | {ports:<18} | {size} bytes"
    )


def main():
    parser = argparse.ArgumentParser(
        description="Capture and display network packet metadata."
    )
    parser.add_argument(
        "-c", "--count", type=int, default=20,
        help="number of packets to capture (default: 20)"
    )
    parser.add_argument(
        "-i", "--interface", default=None,
        help="network interface name (default: Scapy chooses one)"
    )
    args = parser.parse_args()

    if args.count < 1:
        parser.error("count must be at least 1")

    print("\nBASIC NETWORK SNIFFER")
    print("=" * 145)
    print("Capturing packet metadata only. Payload contents are not displayed.")
    print("Use only on networks and devices you own or are authorized to monitor.")
    print("-" * 145)
    print(
        f"{'TIME':<8} | {'PROTOCOL':<14} | {'SOURCE':<39} | "
        f"{'DESTINATION':<39} | {'PORTS':<18} | SIZE"
    )
    print("-" * 145)

    try:
        sniff(
            count=args.count,
            iface=args.interface,
            prn=lambda packet: print(describe_packet(packet)),
            store=False,
            promisc=False,
        )
    except PermissionError:
        print("\nPermission denied. Run with the required packet-capture privileges.")
    except OSError as error:
        print(f"\nCapture error: {error}")
    except KeyboardInterrupt:
        print("\nCapture stopped by user.")
    finally:
        print("\nCapture session finished.")


if __name__ == "__main__":
    main()
