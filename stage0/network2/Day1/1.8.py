import ipaddress
address = input("Enter ipV6 address : ") or "2001:0db8:0000:0000:0000:ff00:0042:8329"
ip = ipaddress.IPv6Address(address)
compreses = ip.compressed
expanded = ip.exploded
print(compreses , end="\n")
print(expanded , end="\n")

