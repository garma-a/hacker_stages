import socket
import struct
import random

def build_dns_query(domain):
    transaction_id = random.randint(0, 65535)
    flags = 0x0100
    questions = 1
    answer_rrs = 0
    authority_rrs = 0
    additional_rrs = 0
    header = struct.pack('!HHHHHH', 
                         transaction_id, 
                         flags, 
                         questions, 
                         answer_rrs, 
                         authority_rrs, 
                         additional_rrs)
    question = b''
    for part in domain.split('.'):
        question += struct.pack('B', len(part))  # Length byte
        question += part.encode('ascii')         # Domain part
    question += b'\x00'  # Null terminator
    question += struct.pack('!HH', 1, 1)
    return header + question, transaction_id

def send_dns_query(domain, dns_server='8.8.8.8', port=53):
    print(f"[*] Building DNS query for: {domain}")
    query, transaction_id = build_dns_query(domain)
    print(f"[*] Transaction ID: {transaction_id}")
    print(f"[*] Query size: {len(query)} bytes")
    print(f"[*] Sending DNS query to {dns_server}:{port}...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5)
    try:
        sock.sendto(query, (dns_server, port))
        print(f"[+] Query sent successfully")
        response, addr = sock.recvfrom(512)
        print(f"[+] Received response from {addr}")
        print(f"[+] Response size: {len(response)} bytes")
        print(f"[+] Response (hex): {response.hex()}")
        resp_id = struct.unpack('!H', response[0:2])[0]
        print(f"[+] Response Transaction ID: {resp_id}")
        if resp_id == transaction_id:
            print(f"[+] Transaction ID matches!")
        else:
            print(f"[-] Transaction ID mismatch!")
    except socket.timeout:
        print("[-] Request timed out")
    except Exception as e:
        print(f"[-] Error: {e}")
    finally:
        sock.close()

domain = input("Enter the domain to query (e.g., example.com): ")
send_dns_query(domain)

