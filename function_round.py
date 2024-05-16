import numpy as np
from function_MixColone import mixColome
from function_MixRow import mixRow
from function_split_by_n import split_by_n
from function_to_matrix44 import to_matrix44


def round(file: bytes, rKey: bytes) -> bytearray:
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