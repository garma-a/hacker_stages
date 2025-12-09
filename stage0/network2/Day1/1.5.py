from typing import List


def first_last_address(ip:str , mask:str)->List[str]:
    ip_parts , mask_parts= list(map(int,ip.split("."))) , list(map(int , mask.split(".")))
    firs_addr , last_addr = [] , []
    for i in range(4):
        firs_addr.append( ip_parts[i] & mask_parts[i])
        last_addr.append(ip_parts[i] | (~mask_parts[i] & 0xFF))
    return [".".join(map(str,firs_addr)) , ".".join(map(str,last_addr))]

print(first_last_address("205.16.37.39" , "255.255.255.240"))










