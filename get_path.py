from tkinter import filedialog


def get_path(file_type: str, file_extension: str) -> str:

    file_path = filedialog.asksaveasfilename(
        defaultextension=file_extension, filetypes=[(file_type, file_extension)])
    return file_path

print(get_path("text",".txt"))