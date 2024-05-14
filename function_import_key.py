import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog, ttk, Radiobutton, IntVar

def import_key() -> None:
    global key, key_label, key_file
    key_file = filedialog.askopenfilename(filetypes=[("Key Files", "*.key")])
    if key_file:
        # key_label.config(text=f"Fichier sélectionné : {key_file}")
        with open(key_file, 'rb') as file:
            key = file.read()
            print(f"Clé importée : {key}")

import_key()
print(key)