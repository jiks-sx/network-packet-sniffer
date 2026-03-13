# Network Packet Sniffer with Alert System

A Python-based **Network Packet Sniffer and Intrusion Detection System (IDS)** built using Scapy.
This project captures live network traffic, analyzes packets, detects suspicious activities like **port scanning and traffic floods**, and logs the data for analysis.

---

## Features

* Real-time packet sniffing using **Scapy**
* Detection of **Port Scanning attacks**
* Detection of **Traffic Flood**
* **DNS query monitoring**
* **Hostname and Reverse DNS lookup**
* **Service detection from ports**
* Packet logging using **SQLite database**
* **Traffic visualization dashboard**
* Filters background protocols like **ARP and ICMP**

---

## Technologies Used

* Python3
* Scapy
* SQLite
* Matplotlib
* Kali Linux(VMware)

---

## Project Structure

```
network-packet-sniffer/
│
├── sniffer.py          # Main packet capture engine
├── detector.py         # Attack detection logic
├── database.py         # Packet logging system
├── network_utils.py    # DNS, hostname and service utilities
├── dashboard.py        # Traffic visualization dashboard
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## Installation

Clone the repository:

```
git clone https://github.com/jiks-sx/network-packet-sniffer.git
```

Move into the project directory:

```
cd network-packet-sniffer
```

Create virtual environment:

```
python3 -m venv venv
```

Activate environment:

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Run the Packet Sniffer

```
sudo python3 sniffer.py
```

---

## Example Output

```
Source IP: 192.168.145.2
Destination IP: 192.168.145.128
Hostname: Unknown
Reverse DNS: 192.168.145.2
Source Port: 443
Destination Port: 36512
Service: https
```

---

## Testing

Generate network traffic:

```
ping google.com
```

Or simulate a port scan:

```
nmap -p 1-200 <your-ip>
```

---

## Dashboard

To visualize captured traffic:

```
python3 dashboard.py
```

This displays a graph showing **packet activity by source IP**.

---

## Use Cases

* Network monitoring
* Security learning and experimentation
* Detecting suspicious network behavior
* Understanding packet-level traffic analysis

---

## Future Improvements

* GeoIP location detection
* Real-time dashboard
* Web-based monitoring interface
* Advanced intrusion detection rules

---

## Author

GitHub: https://github.com/jiks-sx
