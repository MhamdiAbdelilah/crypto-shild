import os

def generate_key(n) -> bytes:
    return os.urandom(n)

print(generate_key(16))