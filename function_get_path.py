from tkinter import filedialog

def get_path(file_type: str, file_extension: str) -> str:
    """ Cette fonction get_path sert a  ouvrir une boîte de dialogue permettant à l'utilisateur de sélectionner un emplacement de fichier.
    Elle demande à l'utilisateur de choisir un emplacement et un nom de fichier avec une extension à préciser, puis retourne le chemin complet du fichier sélectionné."""
    file_path = filedialog.asksaveasfilename(
        defaultextension=file_extension, filetypes=[(file_type, file_extension)])
    return file_path

print(get_path("text",".txt"))