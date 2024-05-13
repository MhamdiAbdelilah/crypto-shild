import hashlib
import os


def generate_key(n) -> bytes:
    return os.urandom(n)


def create_subkey(main_key, identifier: str, nbr: int) -> bytes:
    # Combine the main key with a unique identifier
    combined = main_key + identifier.encode()
    subkey = hashlib.sha256(combined).digest()[:nbr]
    return subkey


key = generate_key(16)  # 16 octe

exmple_key = b'\xc3\xce\xcad\x84\x82\x04\x90\xb5\xbf\x87\xc7\xbcZ\x99\x04'
rkey = create_subkey(exmple_key, 'fiole', 16)  # 16 octe round key


print(f'random key {key}')
print(f'generate round key {rkey}')
