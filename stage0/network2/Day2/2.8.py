import socket

start_port =1
end_port =1023
ip = input("Enter the target IP address: ")

open_ports = []
for port in range(start_port, end_port + 1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        if s.connect_ex((ip, port)) == 0:
            open_ports.append(port)

print(f"Open ports on {ip} from {start_port} to {end_port}: {open_ports}")
