import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("packets.db")
cursor = conn.cursor()

cursor.execute("SELECT src_ip, COUNT(*) FROM packets GROUP BY src_ip")
data = cursor.fetchall()

ips = []
counts = []

for row in data:
    ips.append(row[0])
    counts.append(row[1])

plt.bar(ips, counts)

plt.xlabel("Source IP")
plt.ylabel("Packet Count")
plt.title("Network Traffic Analysis")

plt.show()
