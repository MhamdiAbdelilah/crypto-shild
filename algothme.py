import hashlib
from tkinter import filedialog
import numpy as np
import os


def import_file(path: str) -> bytes:
    with open(path, 'rb') as file:
        return file.read()


def export_file(path: str, content: bytes):

    # remove extantion
    dot_index = path.rfind('.')
    if dot_index > 0:
        extention: str = path[dot_index:]
        path: str = path[:dot_index]
    else:
        extention: str = ''
    try:
        with open(f'{path}{extention}', "xb") as file:
            file.write(content)
            return print("file saved successfully")
    except:
        # try to save file by changing the name
        for i in range(1, 256):
            try:
                with open(f'{path}({i}){extention}', "xb") as file:
                    file.write(content)
                    return print("file saved successfully")
            except:
                continue
        else:
            print("Couldn't save the file. All alternative names are taken.")


def add_tag(path) -> str:
    path = path + '.ecr'
    return path


def remove_tag(path) -> str:
    if path.endswith('.ecr'):
        path = path[:-4]
    return path

def get_path(file_type: str ,file_extension: str) -> str:
    file_path = filedialog.asksaveasfilename(defaultextension=file_extension, filetypes=[(file_type, file_extension)])
    return file_path




def split_by_n(rawFile: bytes, n: int):
    xFile = bytearray()
    for i in range(0, len(rawFile), n):
        chunk = rawFile[i:i+n]
        xFile.extend(chunk)
    return xFile


def to_matrix44(array_1D: np.array) -> np.array:
    try:
        array_2D: np.array = array_1D.reshape(4, 4)
    except:
        padding_needed = 16 - array_1D.size
        padded_array = np.pad(array_1D, (0, padding_needed),
                              'constant', constant_values=0)
        array_2D: np.array = padded_array.reshape(4, 4)
    return array_2D


def create_subkey(main_key, identifier: str, nbr: int) -> bytes:
    # Combine the main key with a unique identifier
    combined = main_key + identifier.encode()
    subkey = hashlib.sha256(combined).digest()[:nbr]
    return subkey


def generate_key(n) -> bytes:
    return os.urandom(n)


def round(file: bytes, rKey: bytes) -> bytearray:
    result: bytearray = bytearray()

    for _i in range(0, len(file), 16):
        chunk_byts: bytearray = bytearray(16)
        chunk: bytes = file[_i:_i+16]
        chunk = split_by_n(chunk, 1)

        chunk_np: np.array = np.array(chunk, dtype='S3')
        chunk_matrix = to_matrix44(chunk_np)

        chunk_matrix = mixColome(chunk_matrix, int.from_bytes(rKey,'little'))
        chunk_matrix = mixRow(chunk_matrix, int.from_bytes(rKey, 'little'))

        chunk_byts = chunk_matrix.flatten()

        chunk_byts = bytearray(int(byte) for byte in chunk_byts)
        chunk_byts1 = bytearray(a ^ b for a, b in zip(chunk_byts, rKey))  # XOR

        result.extend(bytes(chunk_byts1))

    return result


def mixColome(matrix: np.array, n: int) -> np.array:
    result: np.array = np.zeros((4, 4), dtype='S3')

    for i in range(len(matrix)):
        for j in range(4):

            result[i][j] = (matrix[i][(j-n) % 4])
    return result


def mixRow(matrix: np.array, n: int) -> np.array:
    result: np.array = np.zeros((4, 4), dtype='S3')
    for i in range(len(matrix)):
        result[i] = matrix[(i-n) % 4]
    return result


def gen_rKeys(key: bytes, identifier: str, nR: int) -> list[bytes]:
    rKeys: list[bytes] = []
    for i in range(nR):
        rKeys.append(create_subkey(key, f'{identifier}{i}', 16))
    return rKeys


def encrypter_file(file: bytes, rKeys: list[bytes], nR: int) -> bytes:
    file_content: bytes = file

    for r in range(nR):
        tour: bytearray = round(file_content, rKeys[r])
        file_content = bytes(tour)

    return file_content

def decrypter_file(file: bytes, rKeys: list[bytes], nR: int) -> bytes:
    file_content: bytes = file

    for r in range(nR):
        tour: bytearray = round(file_content, rKeys[r])
        file_content = bytes(tour)

    return file_content

