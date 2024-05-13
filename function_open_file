from tkinter import filedialog


def open_file() -> None:
    global file,file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        # file_label.config(text=f"Fichier sélectionné : {file_path}") # this line change the label text of file in the interface
        with open(file_path, 'rb') as file:
            file = file.read()

open_file()

print(f'the file path: {file_path}')
print(f"file importée : {file}")