# Step 1: realtime_nids.py (modified to store alerts and serve dashboard)

from flask import Flask, jsonify, render_template
from scapy.all import sniff, IP, TCP, UDP
import threading
import time
import os

app = Flask(__name__)
alerts = []  # This will store alert logs


# === Detection Logic ===
def detect_abnormal(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        src = ip_layer.src
        dst = ip_layer.dst

        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]
            flags = tcp_layer.flags
            # Example: SYN flood
            if flags == 'S':
                log_alert("SYN Packet Detected", src, dst)

        if packet.haslayer(UDP):
            udp_layer = packet[UDP]
            # Example: UDP flood to port 53
            if udp_layer.dport == 53:
                log_alert("UDP Flood on port 53", src, dst)


# === Alert Logger ===
def log_alert(msg, src, dst):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    alert = {
        "timestamp": timestamp,
        "msg": msg,
        "src": src,
        "dst": dst
    }
    print(f"[ALERT] {msg} from {src} to {dst}")
    alerts.append(alert)
    if len(alerts) > 200:
        alerts.pop(0)  # Keep only last 200


# === Sniffing Thread ===
def start_sniffing():
    sniff(prn=detect_abnormal, store=0)


# === Flask API and Dashboard ===
@app.route('/')
def dashboard():
    return render_template('index.html')


@app.route('/alerts')
def get_alerts():
    return jsonify(alerts=alerts[::-1])


if __name__ == '__main__':
    t = threading.Thread(target=start_sniffing)
    t.daemon = True
    t.start()
    app.run(host='0.0.0.0', port=5000, debug=True)
