import random

mac = []
for _ in range(6):
    byte = random.randint(0x00, 0xFF)
    mac.append(f"{byte:02X}")

print(":".join(mac))

