import socket
import time

def measure_rtt(host, port, message=b"ping"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        start = time.time()
        s.sendall(message)
        data = s.recv(1024)
        end = time.time()
        rtt = (end - start) * 1000  
        return rtt, data
    finally:
        s.close()

rtt, response = measure_rtt("localhost", 9999)
print(f"RTT: {rtt:.2f} ms, Response: {response}")

