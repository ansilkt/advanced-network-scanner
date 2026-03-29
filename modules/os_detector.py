import subprocess

def detect_os(ip):
    try:
        output = subprocess.check_output(f"ping -c 1 {ip}", shell=True).decode()

        if "ttl=64" in output.lower():
            return "Linux/Unix"
        elif "ttl=128" in output.lower():
            return "Windows"
        else:
            return "Unknown"
    except:
        return "Unknown"
