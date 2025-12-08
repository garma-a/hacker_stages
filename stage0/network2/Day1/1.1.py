given_ip_address = "some ip address"

if ":" in given_ip_address:
    parts = given_ip_address.split(":")

    if 2<= len(parts) <=8 :
        print("IPv6")

elif "." in given_ip_address:

    parts = given_ip_address.split(".")

    if len(parts)==4 and all(p.isdigit() and 0<= int(p) <= 255 for p in parts):
        print("Ipv4")
else:
    print("invalid")


# the non-manual way 

import ipaddress

ip_obj = ipaddress.ip_address(given_ip_address)
if isinstance(ip_obj , ipaddress.IPv4Address):
    print("Ipv4")
elif isinstance(ip_obj , ipaddress.IPv6Address):
    print("Ipv6")
