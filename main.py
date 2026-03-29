from modules.host_discovery import scan_network
from modules.port_scanner import scan_ports
from modules.service_detector import detect_service
from modules.os_detector import detect_os
import json

def main():
    base_ip = input("Enter base IP (e.g., 192.168.1): ")

    hosts = scan_network(base_ip)

    full_report = []

    for host in hosts:
        print(f"\nScanning {host}...")

        ports = scan_ports(host)
        os_type = detect_os(host)

        services = {}
        for port in ports:
            banner = detect_service(host, port)
            services[port] = banner

        host_data = {
            "ip": host,
            "os": os_type,
            "open_ports": ports,
            "services": services
        }

        full_report.append(host_data)

    # Save report
    with open("reports/report.json", "w") as f:
        json.dump(full_report, f, indent=4)

    print("\n[✔] Scan completed. Report saved in reports/report.json")

if __name__ == "__main__":
    main()
