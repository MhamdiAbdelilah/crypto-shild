
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter

def develop_keys(main_key_size):
    # Générer une clé principale aléatoire
    main_key = b'<\xd3\x08uv\x86\x18\xa7\xac\x84\xc9fh!\x0e\x1c'
    
    # Initialiser un compteur pour le mode CTR
    ctr = Counter.new(128)
    
    # Créer un objet AES en mode CTR
    cipher = AES.new(main_key, AES.MODE_CTR, counter=ctr)
    
    # Déterminer le nombre de sous-clés en fonction de la taille de la clé principale
    subkeys_count = {128: 8, 192: 12, 256: 16}[main_key_size]
    
    # Générer les sous-clés
    subkeys = [cipher.encrypt(get_random_bytes(main_key_size // 8)) for _ in range(subkeys_count)]
    print (main_key)
    return main_key, subkeys

# Demander à l'utilisateur de saisir la taille de la clé
taille_cle = int(input("Entrez la taille de la clé en bits (128, 192, 256) : "))

# Vérifier que la taille de la clé est valide
if taille_cle not in [128, 192, 256]:
    print("Taille de clé non valide. Veuillez choisir entre 128, 192 ou 256 bits.")
else:
    # Développer les clés selon la taille de la clé principale
    key, subkeys = develop_keys(taille_cle)

    # Afficher la clé principale et les sous-clés
    print(f"Clé à {taille_cle} bits et ses sous-clés :")
    print(key.hex())
    for subkey in subkeys:
        print(subkey.hex())
