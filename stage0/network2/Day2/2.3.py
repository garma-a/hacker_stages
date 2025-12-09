import socket

target_ip = input("Enter the target IP address: ")
open_ports = []
for port in range(1, 1001):
    # IP and TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # i want to skip waiting too long so the max time is 0.5 seconds
        s.settimeout(0.5)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
print(f"Open ports on {target_ip}: {open_ports}")
