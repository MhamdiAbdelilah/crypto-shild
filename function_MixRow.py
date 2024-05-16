import hashlib
from tkinter import filedialog
import numpy as np
import os

def mixRow(matrix: np.array, n: int) -> np.array:
    """ Cette fonction mixRow prend une matrice numpy en entrée et effectue une opération de changement de ligne sur cette matrice.
    Elle décale chaque ligne de la matrice de "n" positions vers le haut , puis retourne la matrice."""
    result: np.array = np.zeros((4, 4), dtype='S3')
    for i in range(len(matrix)):
        result[i] = matrix[(i-n) % 4]
    return result