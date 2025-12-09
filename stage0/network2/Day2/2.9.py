import socket

target = input("Enter the target IP address: ")
start_port = int(input("Enter the start port number (1-65535): "))
end_port = int(input("Enter the end port number (1-65535): "))

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(0.5)
    try:
        sock.sendto(b'', (target, port))
        data, _ = sock.recvfrom(1024)
        print(f"Port {port}: Open (received data)")
    except socket.timeout:
        print(f"Port {port}: Open|Filtered (no response)")
    except socket.error as e:
        if e.errno == 111:  
            print(f"Port {port}: Closed")
        else:
            print(f"Port {port}: Error ({e})")
    finally:
        sock.close()
