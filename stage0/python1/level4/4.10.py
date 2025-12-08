import socket
hostname = "www.google.com"
ip_address = socket.gethostbyname(hostname)
print(f"IP address of {hostname} is {ip_address}")
