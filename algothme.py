
import tkinter as tk
from tkinter import filedialog


def import_file(path):
    with open(path, "rb") as file:  
        return file.read()

def export_file(path, content):
    with open(path, "wb") as file: 
        file.write(content)

def get_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    root.destroy()
    return file_path


print(import_file(get_path()))