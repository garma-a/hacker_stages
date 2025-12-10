def server():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('localhost', 12345))
    data, _ = s.recvfrom(1024)
    print("Message from client: ", data.decode())
    s.close()


def client():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = "Hello, Server!"
    s.sendto(message.encode(), ('localhost', 12345))
    s.close()

#server()
client()
