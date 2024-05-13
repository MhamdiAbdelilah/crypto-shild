import numpy as np


def to_matrix44(array_1D: np.array) -> np.array:
    try:
        array_2D: np.array = array_1D.reshape(4, 4)
    except:
        padding_needed = 16 - array_1D.size
        padded_array = np.pad(array_1D, (0, padding_needed),
                              'constant', constant_values=0)
        array_2D: np.array = padded_array.reshape(4, 4)
    return array_2D


list: np.array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,4,15])
matrix: np.array = to_matrix44(list)
print(matrix)