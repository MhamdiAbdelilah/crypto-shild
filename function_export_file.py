def export_file(path: str, content: bytes) -> None:

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


export_file('file.txt', b'the file should be saved with the name file(1).txt')
