from function_round import round

def encrypter_file(file: bytes, rKeys: list[bytes], nR: int) -> bytes:
    file_content: bytes = file

    for r in range(nR):
        tour: bytearray = round(file_content, rKeys)
        file_content = bytes(tour)

    return file_content

file= b'lakshan'
key = b'\xc3\xce\xcad\x84\x82\x04\x90\xb5\xbf\x87\xc7\xbcZ\x99\x04'

print (encrypter_file(file,key,1))