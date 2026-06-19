
from scapy.all import sniff, IP, conf

conf.L3socket

def analyze_packet(packet):
    if not packet.haslayer(IP):
        return

    ip_layer = packet[IP]

    print("\n--- Packet Captured ---")
    print(f"Source IP: {ip_layer.src}")
    print(f"Destination IP: {ip_layer.dst}")
    print(f"Protocol: {ip_layer.proto}")
    print(packet.summary())

def main():
    print("Capturing packets... Press Ctrl+C to stop.")
    try:
        sniff(filter="ip", prn=analyze_packet, store=False, L2socket=conf.L3socket)
    except KeyboardInterrupt:
        print("\nCapture stopped.")
    except PermissionError:
        print("Error: Run as Administrator.")

if __name__ == "__main__":
    main()



#2nd codd 

from scapy.all import sniff

def packet_callback(packet):
    print("\n--- Packet Captured ---")

    if packet.haslayer("IP"):
        print("Source IP:", packet["IP"].src)
        print("Destination IP:", packet["IP"].dst)
        print("Protocol:", packet["IP"].proto)

    print(packet.summary())

sniff(prn=packet_callback, count=10)
