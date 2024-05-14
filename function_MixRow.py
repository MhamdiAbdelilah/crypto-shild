import hashlib
from tkinter import filedialog
import numpy as np
import os

def mixRow(matrix: np.array, n: int) -> np.array:
    result: np.array = np.zeros((4, 4), dtype='S3')
    for i in range(len(matrix)):
        result[i] = matrix[(i-n) % 4]
    return result