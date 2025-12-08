import random
chars = ['a', 'b', 'c', 'd', 'e' , 'f', 'g', 'h', 'i', 'j' , 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

password = ""
for _ in range(12):
    password += chars[random.randint(0, 25)]

print(password)


