from function_unround import unround


def decrypter_file(encrypted_file: bytes, rKeys: list[bytes], nR: int) -> bytes:
    file_content: bytes = encrypted_file
    # rKeys = rKeys[::-1]
    # Reverse the rounds
    for r in range(nR):
        tour: bytearray = unround(file_content, rKeys)
        file_content = bytes(tour)

    return file_content
file = b'\xc3\xa6\xab\n\x84\x82\x04\x90\xb5\xbf\x87\xc7\xcf6\xf8o'
key = b'\xc3\xce\xcad\x84\x82\x04\x90\xb5\xbf\x87\xc7\xbcZ\x99\x04'

print(decrypter_file(encrypted_file= file,rKeys= key,nR=1))