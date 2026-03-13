from scapy.all import sniff, IP, TCP
from scapy.layers.dns import DNSQR
from database import init_db, log_packet
from detector import detect_attack
from network_utils import get_hostname, get_dns, get_service


def process_packet(packet):

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        src_port = None
        dst_port = None

        # TCP Ports
        if packet.haslayer(TCP):
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

        # Hostname lookup
        hostname = get_hostname(src_ip)

        # Reverse DNS lookup
        dns_lookup = get_dns(src_ip)

        # DNS query (example: google.com)
        dns_query = "None"
        if packet.haslayer(DNSQR):
            dns_query = packet[DNSQR].qname.decode()

        # Service detection
        service = None
        if dst_port:
            service = get_service(dst_port)

        # Attack detection
        alert = detect_attack(src_ip, dst_port)

        # Log packet to database
        log_packet(src_ip, dst_ip, src_port, dst_port, alert)

        print("\n==============================")
        print("Source IP:", src_ip)
        print("Destination IP:", dst_ip)
        print("Hostname:", hostname)
        print("Reverse DNS:", dns_lookup)
        print("DNS Query:", dns_query)
        print("Source Port:", src_port)
        print("Destination Port:", dst_port)
        print("Service:", service)

        if alert != "None":
            print("ALERT:", alert)

        print("==============================\n")


def main():

    print("Starting Packet Sniffer...")

    init_db()

    sniff(prn=process_packet, store=False, filter="tcp")

if __name__ == "__main__":
    main()
