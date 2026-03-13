from collections import defaultdict
import time

packet_count = defaultdict(int)
port_tracker = defaultdict(set)

TIME_WINDOW = 10
FLOOD_THRESHOLD = 200
PORT_SCAN_THRESHOLD = 15

last_reset = time.time()


def detect_attack(src_ip, dst_port):

    global last_reset
    alert = "None"

    # Reset counters periodically
    if time.time() - last_reset > TIME_WINDOW:
        packet_count.clear()
        port_tracker.clear()
        last_reset = time.time()

    # Ignore packets without port (ARP, ICMP etc.)
    if dst_port is None:
        return alert

    # Count packets
    packet_count[src_ip] += 1

    # Track ports accessed
    port_tracker[src_ip].add(dst_port)

    # Flood detection
    if packet_count[src_ip] > FLOOD_THRESHOLD:
        alert = f"Traffic flood from {src_ip}"

    # Port scan detection
    if len(port_tracker[src_ip]) > PORT_SCAN_THRESHOLD:
        alert = f"Port scan detected from {src_ip}"

    return alert
