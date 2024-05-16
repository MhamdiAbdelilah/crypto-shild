
import hashlib
from tkinter import filedialog
import numpy as np

def create_subkey(main_key, identifier: str, nbr: int) -> bytes:
    """Ce code génère une sous-clé à partir d'une clé principale et d'un identifiant unique en utilisant un algorithme de hachage. 
Il extrait ensuite une portion spécifique de ce hachage pour former la sous-clé."""
    combined = main_key + identifier.encode()
    subkey = hashlib.sha256(combined).digest()[:nbr]
    return subkey

print(create_subkey(b'\xc3\xce\xcad\x84\x82\x04\x90\xb5\xbf\x87\xc7\xbcZ\x99\x04','lakshan',16)) 