##PROJECT 1:
# Python TCP Port Scanner

A simple TCP port scanner built using Python.

## Features

- Scan target by IP or domain
- Custom port range
- Adjustable timeout
- Multi-threaded scanning

## Technologies Used

- socket
- argparse
- concurrent.futures (ThreadPoolExecutor)
- datetime

## Usage

Basic scan:

''bash
python portscan.py example.com
python portscan.py 192.168.1.10 --start 1 --end 1024
python portscan.py 127.0.0.1 --start 79 --end 82 --workers 10 --timeout 0.5

## Command-Line Options

- target : Hostname or IP address
- --start : Starting port (default: 1)
- --end : Ending port (default: 65535)
- --workers : Maximum worker threads (default: 100)
- --timeout : Socket timeout in seconds (default: 1.0)

## Legal Notice

Only scan systems you own or have permission to test.
Unauthorized scanning may violate laws or network policies.

## Project Structure

.
├── portscan.py
└── README.md

## What I Learned

- How TCP handshake works
- How multithreading improves scan speed
- Risks of excessive concurrency

##PROJECT 2:

# 🔥 Simple Firewall Simulation (Python)

A basic Python project that simulates firewall rule checking by generating random IP addresses and determining whether they are **ALLOWED** or **BLOCKED** based on predefined firewall rules.

---

## 📌 Project Overview

This project demonstrates a simple firewall simulation using Python.  
It generates random IP addresses within a local network range and checks them against predefined firewall rules.

If the IP address matches a blocked rule, it is marked as **BLOCK**.  
Otherwise, it is **ALLOW**.

---

## 🛠 Technologies Used

- Python 3.x
- Built-in `random` module

---

## 📂 Project Structure

firewall-simulation/
│
├── firewall.py
└── README.md

---

## 🚀 How It Works

1. A random IP address is generated in the range:
192.168.1.0 - 192.168.1.20


2. The program checks the IP address against predefined firewall rules.

3. If the IP exists in the rule set:
- ACTION: `BLOCK`

Otherwise:
- ACTION: `ALLOW`

4. A random system ID (0–9999) is generated.

5. The result is printed in the format:

IP_ADD: <ip_address>, ACTION: <ALLOW/BLOCK>, SYSTEM_ID: <random_id>


---

## 🔒 Firewall Rules Example

python
firewall_rules = {
 "192.168.1.1": "BLOCK",
 "192.168.1.6": "BLOCK",
 "192.168.1.19": "BLOCK",
 "192.168.1.12": "BLOCK",
 "192.168.1.8": "BLOCK",
 "192.168.1.15": "BLOCK"
}


## sample output:

IP_ADD: 192.168.1.12, ACTION: BLOCK, SYSTEM_ID: 9271
IP_ADD: 192.168.1.3, ACTION: ALLOW, SYSTEM_ID: 1844
IP_ADD: 192.168.1.8, ACTION: BLOCK, SYSTEM_ID: 5521

##Project 3:
# 🚨 Real-Time Network Packet Rate Monitor & Auto IP Blocker (Python)

A real-time network monitoring tool built with Python and Scapy that detects high packet rates from source IP addresses and automatically blocks suspicious IPs using iptables.

---

## 📌 Project Overview

This project monitors live network traffic and detects potential flooding or DoS-like behavior by calculating the packet rate per source IP address.

If an IP exceeds the defined packet rate threshold, it is automatically blocked using:

iptables firewall rule:
DROP incoming traffic from that IP.

---

## ⚙️ Features

- Real-time packet sniffing
- Source IP tracking
- Packet rate calculation (per second)
- Automatic IP blocking
- Root privilege verification
- Uses Linux iptables for enforcement

---

## 🛠 Technologies Used

- Python 3.x
- Scapy (packet sniffing)
- iptables (Linux firewall)
- collections.defaultdict
- time, os, sys modules

---

## 📂 Project Structure

network-monitor/
│
├── monitor.py
└── README.md

---

## 🚀 How It Works

1. The script captures live IP packets using Scapy.
2. It counts packets per source IP.
3. Every 1 second:
   - Packet rate = total packets / time interval
4. If packet rate > THRESHOLD:
   - The IP is blocked using:

iptables -A INPUT -s <ip_address> -j DROP

5. Blocked IPs are stored to avoid duplicate rules.

---

## 🔧 Configuration

Default threshold:


This means:
If an IP sends more than 40 packets per second, it will be blocked.

You can modify this value inside the script.

---

## ▶️ Requirements

- Linux OS (iptables required)
- Python 3.x
- Root privileges
- Scapy installed



