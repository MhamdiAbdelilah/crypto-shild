import numpy as np
from function_MixColone import mixColome
from function_MixRow import mixRow
from function_split_by_n import split_by_n
from function_to_matrix44 import to_matrix44


def round(file: bytes, rKey: bytes) -> bytearray:
    """ Cette fonction round effectue un tour du cryptage .
     
    Elle prend en entrée un morceau de fichier et une clé de tour.
    Pour chaque bloc de 16 octets du fichier, elle effectue les étapes suivantes :
    - Divise le bloc en octets individuels.
    - Transforme les octets en une matrice 4x4.
    - Applique l'opération de changement de colonne (mixColome) et l'opération de changement de ligne (mixRow) sur la matrice.
    - Aplati la matrice en un tableau d'octets.
    - Effectue une opération de chiffrement par bloc en utilisant un XOR entre chaque octet du bloc et la clé de tour.
    - Ajoute le bloc chiffré au résultat final.
    Elle retourne le résultat final sous forme de bytearray.
    """
    result: bytearray = bytearray()

    for _i in range(0, len(file), 16):
        chunk_byts: bytearray = bytearray(16)
        chunk: bytes = file[_i:_i+16]
        chunk = split_by_n(chunk, 1)

        chunk_np: np.array = np.array(chunk, dtype='S3')
        chunk_matrix = to_matrix44(chunk_np)

        chunk_matrix = mixColome(chunk_matrix, 1)
        chunk_matrix = mixRow(chunk_matrix, 3)

        chunk_byts = chunk_matrix.flatten()

        chunk_byts = bytearray(int(byte) for byte in chunk_byts)
        chunk_byts1 = bytearray(a ^ b for a, b in zip(chunk_byts, rKey))  # XOR

        result.extend(bytes(chunk_byts1))


    return result