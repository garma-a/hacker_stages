import socket
import logging

logging.basicConfig(
    filename='tcp_connections.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

HOST = "localhost"
PORT = 9999

server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()
print(f"Listening for incoming TCP connections on port {PORT}...")
while True:
    conn, addr = server.accept()
    logging.info(f"Incoming connection from {addr[0]}:{addr[1]}")
    print(f"Connection from {addr[0]}:{addr[1]}")
    conn.close()


