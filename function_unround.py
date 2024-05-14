
from function_MixColone import mixColome
from function_MixRow import mixRow
import numpy as np # type: ignore
from function_to_matrix44 import to_matrix44


def unround(file: bytes, rKey: bytes) -> bytearray:
    result: bytearray = bytearray()

    for _i in range(0, len(file), 16):
        chunk_byts: bytearray = bytearray(16)
        chunk: bytes = file[_i:_i+16]

        # XOR with rKey
        chunk_byts1 = bytearray(a ^ b for a, b in zip(chunk, rKey))
        
        chunk_np: np.array = np.array(list(chunk_byts1), dtype='S3')
        
        chunk_matrix = to_matrix44(chunk_np)
        chunk_matrix = mixRow(chunk_matrix, -3)
        chunk_matrix = mixColome(chunk_matrix, -1)
        
        chunk_byts = chunk_matrix.flatten()
        chunk_byts = bytearray(int(byte) for byte in chunk_byts)

        result.extend(bytes(chunk_byts))

    return result
file = b"lakshan"
key = b'\xc3\xce\xcad\x84\x82\x04\x90\xb5\xbf\x87\xc7\xbcZ\x99\x04'
print(unround(file , key))