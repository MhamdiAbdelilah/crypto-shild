import os

def generate_key(n) -> bytes:
    """Cette fonction generate_key génère une clé aléatoire de longueur indiqué par l'utilisateur
    Elle retourne la clé générée sous forme de bytes."""
    return os.urandom(n)
print(generate_key(16))