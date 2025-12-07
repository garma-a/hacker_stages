ports_services = {
    20: "FTP Data Transfer",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    6379: "Redis"
}

while True:
        user_input = input("Enter a port number : ")
        port_number = int(user_input)
        service = ports_services.get(port_number, "Unknown port")
        print(f"Port {port_number}: {service}")
