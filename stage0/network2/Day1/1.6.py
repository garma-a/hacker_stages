# 192.168.1.0/24
ip = "192.168.1.0"
network_parts = ip.split(".")
for i in range(1, 255):  
    host_ip = f"{network_parts[0]}.{network_parts[1]}.{network_parts[2]}.{i}"
    print(host_ip)



# the non-manual dynamic way
import ipaddress
subnet = ipaddress.ip_network("192.168.1.0/24")
for ip in subnet.hosts():
    print(ip)






