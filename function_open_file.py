from tkinter import filedialog


def open_file() -> None:
    """ Cette fonction open_file sert a ouvrir une boîte de dialogue permettant à l'utilisateur de sélectionner un fichier.
    Elle stocke le chemin du fichier sélectionné dans la variable globale file_path et lit le contenu du fichier en mode lecture binaire.
    Ensuite, elle stocke le contenu du fichier dans la variable file.
    Elle affiche ensuite le chemin du fichier sélectionné et son contenu."""
    global file,file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        # file_label.config(text=f"Fichier sélectionné : {file_path}") # this line change the label text of file in the interface
        with open(file_path, 'rb') as file:
            file = file.read()
open_file()

print(f'the file path: {file_path}')
print(f"file importée : {file}")