import socket
import struct
import sys

# Protocol numbers
PROTOCOL_TCP = 6
PROTOCOL_UDP = 17

def main():
    try:
        # Create raw socket to capture all packets
        # AF_PACKET for Linux, AF_INET with IPPROTO_IP for Windows
        if sys.platform.startswith('linux'):
            conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        else:
            conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
            conn.bind(('0.0.0.0', 0))
            conn.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            # Enable promiscuous mode on Windows
            #conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        print("[*] Packet Sniffer Started. Press Ctrl+C to stop.")
        print("-" * 80)
        packet_count = 0
        while True:
            raw_data, addr = conn.recvfrom(65535)
            # For Linux, skip Ethernet header (14 bytes)
            if sys.platform.startswith('linux'):
                eth_header = raw_data[:14]
                eth_protocol = struct.unpack('!H', eth_header[12:14])[0]
                # Only process IPv4 packets (0x0800)
                if eth_protocol != 0x0800:
                    continue
                ip_header = raw_data[14:34]
            else:
                ip_header = raw_data[:20]
            # Parse IP header
            ip_data = parse_ip_header(ip_header)
            
            # Only process TCP and UDP packets
            if ip_data['protocol'] == PROTOCOL_TCP:
                packet_count += 1
                print(f"\n[Packet #{packet_count}] TCP Packet")
                print_ip_info(ip_data)
                
                if sys.platform.startswith('linux'):
                    tcp_header = raw_data[34:54]
                else:
                    tcp_header = raw_data[20:40]
                
                tcp_data = parse_tcp_header(tcp_header)
                print_tcp_info(tcp_data)
                
            elif ip_data['protocol'] == PROTOCOL_UDP:
                packet_count += 1
                print(f"\n[Packet #{packet_count}] UDP Packet")
                print_ip_info(ip_data)
                
                if sys.platform.startswith('linux'):
                    udp_header = raw_data[34:42]
                else:
                    udp_header = raw_data[20:28]
                
                udp_data = parse_udp_header(udp_header)
                print_udp_info(udp_data)
            
            print("-" * 80)
                
    except KeyboardInterrupt:
        print("\n\n[*] Stopping packet sniffer...")
        if not sys.platform.startswith('linux'):
            #conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        #sys.exit(0)
    except PermissionError:
        print("[!] Error: This script requires root/administrator privileges")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)

def parse_ip_header(ip_header):
    """Parse IP header and extract relevant information"""
    # Unpack IP header (first 20 bytes)
    ip_header_unpacked = struct.unpack('!BBHHHBBH4s4s', ip_header)
    
    version_ihl = ip_header_unpacked[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF
    
    ttl = ip_header_unpacked[5]
    protocol = ip_header_unpacked[6]
    src_ip = socket.inet_ntoa(ip_header_unpacked[8])
    dst_ip = socket.inet_ntoa(ip_header_unpacked[9])
    
    return {
        'version': version,
        'header_length': ihl * 4,
        'ttl': ttl,
        'protocol': protocol,
        'src_ip': src_ip,
        'dst_ip': dst_ip
    }

def parse_tcp_header(tcp_header):
    """Parse TCP header and extract relevant information"""
    tcp_header_unpacked = struct.unpack('!HHLLBBHHH', tcp_header)
    
    src_port = tcp_header_unpacked[0]
    dst_port = tcp_header_unpacked[1]
    sequence = tcp_header_unpacked[2]
    acknowledgment = tcp_header_unpacked[3]
    flags = tcp_header_unpacked[5]
    
    # Extract flag bits
    flag_urg = (flags & 32) >> 5
    flag_ack = (flags & 16) >> 4
    flag_psh = (flags & 8) >> 3
    flag_rst = (flags & 4) >> 2
    flag_syn = (flags & 2) >> 1
    flag_fin = flags & 1
    
    return {
        'src_port': src_port,
        'dst_port': dst_port,
        'sequence': sequence,
        'acknowledgment': acknowledgment,
        'flags': {
            'URG': flag_urg,
            'ACK': flag_ack,
            'PSH': flag_psh,
            'RST': flag_rst,
            'SYN': flag_syn,
            'FIN': flag_fin
        }
    }

def parse_udp_header(udp_header):
    """Parse UDP header and extract relevant information"""
    udp_header_unpacked = struct.unpack('!HHHH', udp_header)
    
    src_port = udp_header_unpacked[0]
    dst_port = udp_header_unpacked[1]
    length = udp_header_unpacked[2]
    
    return {
        'src_port': src_port,
        'dst_port': dst_port,
        'length': length
    }

def print_ip_info(ip_data):
    """Print IP header information"""
    print(f"  Source IP: {ip_data['src_ip']}")
    print(f"  Destination IP: {ip_data['dst_ip']}")
    print(f"  TTL: {ip_data['ttl']}")

def print_tcp_info(tcp_data):
    """Print TCP header information"""
    print(f"  Source Port: {tcp_data['src_port']}")
    print(f"  Destination Port: {tcp_data['dst_port']}")
    print(f"  Sequence: {tcp_data['sequence']}")
    print(f"  Acknowledgment: {tcp_data['acknowledgment']}")
    
    # Print active flags
    active_flags = [flag for flag, value in tcp_data['flags'].items() if value]
    if active_flags:
        print(f"  Flags: {', '.join(active_flags)}")

def print_udp_info(udp_data):
    """Print UDP header information"""
    print(f"  Source Port: {udp_data['src_port']}")
    print(f"  Destination Port: {udp_data['dst_port']}")
    print(f"  Length: {udp_data['length']} bytes")

