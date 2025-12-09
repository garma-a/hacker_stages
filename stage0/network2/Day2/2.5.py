import random

def generate_open_ports(n=5, start=1024, end=65535):
    return random.sample(range(start, end + 1), n)
