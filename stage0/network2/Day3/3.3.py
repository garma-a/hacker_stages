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

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 9999))
    data = s.recv(1024)
    print(f"Message from server: {data.decode()}")
    s.close()


#server()
client()
