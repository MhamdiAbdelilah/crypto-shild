def export_file(path: str, content: bytes) -> None:
    """ Cette fonction export_file enregistre le contenu binaire passé en paramètre dans un fichier défini par le chemin.
    Elle ouvre le fichier en mode écriture binaire, écrit le contenu dans le fichier, puis ferme le fichier.
    elle affiche un message indiquant que le fichier a été enregistré avec succès."""
    with open(f'{path}', "wb") as file:
        file.write(content)
        return print("file saved successfully")


export_file('file.txt', b'the file should be saved with the name file(1).txt')
