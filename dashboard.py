import tkinter as tk
from tkinter import ttk
import sqlite3
import threading
import os

def run_sniffer():
    os.system("sudo python3 sniffer.py")

def run_detector():
    os.system("python3 detector.py")

def show_graph():
    os.system("python3 graph.py")

def update_table():

    conn = sqlite3.connect("packets.db")
    cursor = conn.cursor()

    cursor.execute("SELECT src_ip, dst_ip, protocol, length FROM packets ORDER BY id DESC LIMIT 30")
    rows = cursor.fetchall()

    for row in table.get_children():
        table.delete(row)

    for r in rows:

        tag = ""

        if r[3] > 1000:
            tag = "attack"

        table.insert("", tk.END, values=r, tags=(tag,))

    conn.close()

    update_attack_counter()

    root.after(3000, update_table)


def update_attack_counter():

    conn = sqlite3.connect("packets.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM packets")
    count = cursor.fetchone()[0]

    counter_label.config(text=f"Total Packets: {count}")

    conn.close()


def show_alerts():

    try:
        with open("alerts.log","r") as f:
            data = f.read()
            alert_box.delete(1.0, tk.END)
            alert_box.insert(tk.END, data)
    except:
        alert_box.insert(tk.END,"No alerts yet")


root = tk.Tk()

root.title("Cyber Security SOC Dashboard")
root.geometry("1200x650")
root.configure(bg="#111111")

title = tk.Label(root,text="Real Time Network Intrusion Detection System",
                 font=("Arial",16),fg="lime",bg="#111111")

title.pack(pady=10)

counter_label = tk.Label(root,text="Total Packets: 0",
                         font=("Arial",12),fg="white",bg="#111111")

counter_label.pack()

button_frame = tk.Frame(root,bg="#111111")
button_frame.pack(pady=10)

btn1 = tk.Button(button_frame,text="Start Sniffer",command=lambda: threading.Thread(target=run_sniffer).start(),bg="black",fg="lime")
btn1.grid(row=0,column=0,padx=10)

btn2 = tk.Button(button_frame,text="Start Detector",command=lambda: threading.Thread(target=run_detector).start(),bg="black",fg="lime")
btn2.grid(row=0,column=1,padx=10)

btn3 = tk.Button(button_frame,text="Traffic Graph",command=show_graph,bg="black",fg="lime")
btn3.grid(row=0,column=2,padx=10)

btn4 = tk.Button(button_frame,text="Show Alerts",command=show_alerts,bg="black",fg="lime")
btn4.grid(row=0,column=3,padx=10)

columns = ("Source IP","Destination IP","Protocol","Length")

table = ttk.Treeview(root,columns=columns,show="headings",height=18)

for col in columns:
    table.heading(col,text=col)
    table.column(col,width=200)

table.tag_configure("attack", background="red")

table.pack(pady=20)

alert_label = tk.Label(root,text="Alerts",fg="lime",bg="#111111")
alert_label.pack()

alert_box = tk.Text(root,height=8,width=110,bg="black",fg="lime")
alert_box.pack()

update_table()

root.mainloop()
