import hashlib
from tkinter import filedialog
import numpy as np
import os
def mixColome(matrix: np.array, n: int) -> np.array:
    result: np.array = np.zeros((4, 4), dtype='S3')

    for i in range(len(matrix)):
        for j in range(4):

            result[i][j] = (matrix[i][(j-n) % 4])
    return result