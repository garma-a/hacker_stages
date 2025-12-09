import socket

port = int(input("Enter the port number to check (1-65535): "))

tcp_ports = {20, 21, 22, 23, 25, 80, 110, 143, 443, 3389}
udp_ports = {53, 67, 68, 69}

if port in tcp_ports:
    print("TCP")
elif port in udp_ports:
    print("UDP")
else:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_sock:
            tcp_sock.bind(('', port))
        print("TCP")
    except OSError:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_sock:
                udp_sock.bind(('', port))
            print("UDP")
        except OSError:
            print("Unknown")

