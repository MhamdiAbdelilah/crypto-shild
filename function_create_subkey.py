
import hashlib
from tkinter import filedialog
import numpy as np

def create_subkey(main_key, identifier: str, nbr: int) -> bytes:
    # Combine the main key with a unique identifier
    combined = main_key + identifier.encode()
    subkey = hashlib.sha256(combined).digest()[:nbr]
    return subkey

print(create_subkey(b'\xc3\xce\xcad\x84\x82\x04\x90\xb5\xbf\x87\xc7\xbcZ\x99\x04','lakshan',16)) 