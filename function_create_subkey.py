
import hashlib
from tkinter import filedialog
import numpy as np

def create_subkey(main_key, identifier: str, nbr: int) -> bytes:
    # Combine the main key with a unique identifier
    combined = main_key + identifier.encode()
    subkey = hashlib.sha256(combined).digest()[:nbr]
    return subkey
print(create_subkey)

