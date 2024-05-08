import tkinter as tk
from tkinter import filedialog
import numpy as np
import os


def import_file(path: str):
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


def add_tag(path):
    path = path + '.ecr'
    return path


def remove_tag(path):
    if path.endswith('.ecr'):
        path = path[:-4]
    return path


def get_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    root.destroy()
    return file_path


def split_by_n(rawFile: bytes, n: int):
    xFile = bytearray()
    for i in range(0, len(rawFile), n):
        chunk = rawFile[i:i+16]
        xFile.extend(chunk)
    return xFile


def to_matrix44(file: np.array):
    list = np.reshape(file, 4, 4)
    return list


def expand_key(key: bytes) -> list[bytes]:
    rKey: list[bytes] = []

    return rKey

def generate_key() -> bytes:
    return os.urandom(16)

def round(matrix: bytes, rKey: bytes) -> None:

    # save the list in xfile
    xfile.extend(bytes(matrix))




file_path: str = get_path()
file: str = import_file(file_path)
file_list: bytearray = split_by_n(file, 16)
# import the key here
key_path: str = get_path()
key: str = import_file(key_path)

# genart round key
rkeys = expand_key(key)

# declar the arry where we save the result of encreption or decreption
xfile = bytearray([])

for i in range(len(file_list)):
    list1: bytearray = split_by_n(file_list[i],1)
    list1 = np.array(list1)
    try:
        matrix = np.reshape(list1, (4, 4))
    except:
        matrix = np.array(list1)
    # the round shoud start from here
    round(matrix, rkeys[i])
    # to her


# the last round here


print(xfile)
