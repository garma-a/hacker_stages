import queue
import time
import threading

client_to_server = queue.Queue()
server_to_client = queue.Queue()

def server():
    print("[Server] Waiting for SYN...")
    msg = client_to_server.get()
    if msg == "SYN":
        print("[Server] Received SYN")
        print("[Server] Sending SYN-ACK")
        server_to_client.put("SYN-ACK")
        msg = client_to_server.get()
        if msg == "ACK":
            print("[Server] Received ACK")
            print("[Server] Handshake complete")

def client():
    time.sleep(0.5) 
    print("[Client] Sending SYN")
    client_to_server.put("SYN")
    msg = server_to_client.get()
    if msg == "SYN-ACK":
        print("[Client] Received SYN-ACK")
        print("[Client] Sending ACK")
        client_to_server.put("ACK")
        print("[Client] Handshake complete")

server_thread = threading.Thread(target=server)
client_thread = threading.Thread(target=client)

server_thread.start()
client_thread.start()

server_thread.join()
client_thread.join()
