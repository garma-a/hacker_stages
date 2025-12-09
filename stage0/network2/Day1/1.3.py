with open("Extract_all_IP_text_file.txt" , 'r') as file:
     content = file.read()

def is_ip(s:str)->bool:
    parts = s.split(".")
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
    return len(parts) == 4


words = content.split()
ip_addresses = [word for word in words if is_ip(word)]
print(ip_addresses)





