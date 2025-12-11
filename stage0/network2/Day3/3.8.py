import socket

def test_telnet(host, port=23, timeout=5):
    try:
        print(f"[*] Testing telnet connection to {host}:{port}...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"[+] SUCCESS: Port {port} is open on {host}")
            print(f"[+] Telnet access is allowed")
            sock.close()
            return True
        else:
            print(f"[-] FAILED: Port {port} is closed or filtered on {host}")
            sock.close()
            return False
    except socket.gaierror:
        print(f"[-] ERROR: Could not resolve hostname {host}")
        return False
    except socket.timeout:
        print(f"[-] TIMEOUT: Connection to {host}:{port} timed out")
        return False
    except Exception as e:
        print(f"[-] ERROR: {e}")
        return False

host = input("Enter the target host (IP or domain): ")

test_telnet(host)

