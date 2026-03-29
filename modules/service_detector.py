import socket

def detect_service(ip, port):
    s = socket.socket()
    s.settimeout(2)

    try:
        s.connect((ip, port))
        s.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = s.recv(1024).decode(errors="ignore")
        return banner.strip()
    except:
        return "Unknown"
    finally:
        s.close()
