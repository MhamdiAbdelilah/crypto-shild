
def split_by_n(rawFile: bytes, n: int):
    """ Cette fonction split_by_n divise une chaîne d'octets en segments de taille indiqué.
    Elle prend une chaîne d'octets et un entier "n" en entrée, puis itère sur la chaîne d'octets en découpant la chaîne en segments de taille "n".
    Elle affiche chaque segment découpé et étend une nouvelle chaîne d'octets avec chaque segment.
    Enfin, elle retourne la nouvelle chaîne d'octets contenant tous les segments."""
    xFile = bytearray()
    for i in range(0, len(rawFile), n):
        chunk = rawFile[i:i+n]
        print(chunk)
        xFile.extend(chunk)
    return xFile

file: bytes = b'\xc3\xce\xcad\x84\x82\x04\x90\xb5\xbf\x87\xc7\xbcZ\x99\x04'
file_bytearray = split_by_n(file,2)
print(file_bytearray)