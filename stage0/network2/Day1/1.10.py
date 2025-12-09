import ipaddress

ip1 = input("enter the first ip : ")
ip2 = input("enter the second ip : ")
prefix_length = input("enter the prefix length : ")

net1 = ipaddress.ip_network(f"{ip1}/{prefix_length}")
net2 = ipaddress.ip_network(f"{ip2}/{prefix_length}")

print("the same subnet" if net1.network_address == net2.network_address  else "not the same" )




