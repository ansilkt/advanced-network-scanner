:::writing{variant=“standard” id=“48392”}

🔍 Advanced Network Scanner & Enumeration Tool

📌 Overview

A Python-based tool designed to perform network reconnaissance and attack surface mapping.
It identifies live hosts, scans open ports, detects services, and performs OS fingerprinting.

🚀 Features
	•	Host discovery (Ping sweep)
	•	Port scanning (multithreaded)
	•	Service detection (banner grabbing)
	•	OS fingerprinting
	•	JSON report generation

🛠️ Tech Stack
	•	Python
	•	Socket Programming
	•	Multithreading

▶️ Usage
python main.py
📊 Sample Output
{
  "ip": "192.168.1.1",
  "open_ports": [22, 80],
  "services": {
    "22": "OpenSSH",
    "80": "Apache"
  }
}
⚠️ Disclaimer

This tool is for educational purposes only. Do not use it on networks without permission.
:::

