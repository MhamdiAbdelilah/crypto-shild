
def split_by_n(rawFile: bytes, n: int):
    xFile = bytearray()
    for i in range(0, len(rawFile), n):
        chunk = rawFile[i:i+n]
        print(chunk)
        xFile.extend(chunk)
    return xFile


file: bytes = b'\xc3\xce\xcad\x84\x82\x04\x90\xb5\xbf\x87\xc7\xbcZ\x99\x04'
file_bytearray = split_by_n(file,2)
print(file_bytearray)