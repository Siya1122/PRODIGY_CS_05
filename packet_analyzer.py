from scapy.all import sniff

def packet_callback(packet):
    print("\n--- Packet Captured ---")

    if packet.haslayer("IP"):
        print("Source IP:", packet["IP"].src)
        print("Destination IP:", packet["IP"].dst)
        print("Protocol:", packet["IP"].proto)

    print(packet.summary())

sniff(prn=packet_callback, count=10)
