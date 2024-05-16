import hashlib
from tkinter import filedialog
import numpy as np
import os
def mixColome(matrix: np.array, n: int) -> np.array:
    """ Cette fonction mixColome prend une matrice numpy en entrée et effectue une opération de changement de colonne sur cette matrice.
    Elle décale chaque élément de chaque colonne de la matrice de "n" positions vers la gauche , puis retourne la matrice."""
    result: np.array = np.zeros((4, 4), dtype='S3')

    for i in range(len(matrix)):
        for j in range(4):

            result[i][j] = (matrix[i][(j-n) % 4])
    return result
