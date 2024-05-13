import hashlib
import os

def generate_key(n: int) -> bytes:
    return os.urandom(n)

def create_subkey(main_key, identifier: str, nbr: int) -> bytes:
    # Combine the main key with a unique identifier
    combined = main_key + identifier.encode()
    subkey = hashlib.sha256(combined).digest()[:nbr]
    return subkey
def gen_rKeys(key: bytes, identifier: str, nR: int) -> list[bytes]:
    rKeys: list[bytes] = []
    for i in range(nR):
        rKeys.append(create_subkey(key, f'{identifier}{i}', 16))
    return rKeys

# test du code pour generer des cles 
# key = generate_key(16)
# rKeys =gen_rKeys(key ,"a",8)
# print(key)
# print(rKeys)