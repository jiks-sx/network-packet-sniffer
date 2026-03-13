import sqlite3
from datetime import datetime


def init_db():
    conn = sqlite3.connect("packets.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS packet_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            src_ip TEXT,
            dst_ip TEXT,
            src_port INTEGER,
            dst_port INTEGER,
            alert TEXT
        )
    """)

    conn.commit()
    conn.close()
    print("Database Created Successfully")


def log_packet(src_ip, dst_ip, src_port, dst_port, alert):

    conn = sqlite3.connect("packets.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO packet_logs
        (timestamp, src_ip, dst_ip, src_port, dst_port, alert)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        src_ip,
        dst_ip,
        src_port,
        dst_port,
        alert
    ))

    conn.commit()
    conn.close()
