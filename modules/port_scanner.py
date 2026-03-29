import socket
from concurrent.futures import ThreadPoolExecutor

common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080]

def scan_port(ip, port):
    s = socket.socket()
    s.settimeout(1)

    try:
        s.connect((ip, port))
        return port
    except:
        return None
    finally:
        s.close()

def scan_ports(ip):
    open_ports = []

    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(lambda p: scan_port(ip, p), common_ports)

    for port in results:
        if port:
            print(f"[+] {ip}:{port} open")
            open_ports.append(port)

    return open_ports
