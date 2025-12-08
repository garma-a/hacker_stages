sample_ip = "192.168.1.1"
parts = sample_ip.split(".")
binary_result=""
for part in parts:
    binary_part = format(int(part) , "08b")
    binary_result+=binary_part
print(binary_result)


