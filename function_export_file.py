def export_file(path: str, content: bytes) -> None:

    with open(f'{path}', "wb") as file:
        file.write(content)
        return print("file saved successfully")


export_file('file.txt', b'the file should be saved with the name file(1).txt')
