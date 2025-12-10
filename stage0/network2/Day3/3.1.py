# Write a simple TCP client-server program that sends a message from client to server.
# Server Code
# i will run this on the first teminal 
# to create the TCP server 
#------------------------------------
#------------------------------------
from os import close


def server():
    import socket
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.bind(('localhost', 12345))
    s.listen(1)
    conn , _ = s.accept()
    data = conn.recv(1024)
    print("Message from client: ", data.decode())
    conn.close()
    s.close()
#------------------------------------
#------------------------------------
# Client Code
# i will run this in the second terminal
# to create the TCP client and send message to the server
#------------------------------------
#------------------------------------
def client():
    import socket
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect(('localhost', 12345))
    message = "Hello, Server!"
    s.send(message.encode())
    s.close()





#server()
client()

