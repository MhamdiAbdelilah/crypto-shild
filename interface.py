import tkinter as tk
import algothme as al
from tkinter import filedialog, ttk, Radiobutton, IntVar


def open_file() -> None:
    global file,file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        file_label.config(text=f"Fichier sélectionné : {file_path}")
        with open(file_path, 'rb') as file:
            file = file.read()
            # print(f"file importée : {file}")


def import_key() -> None:
    global key
    key_file = filedialog.askopenfilename(filetypes=[("Key Files", "*.key")])
    if key_file:
        key_label.config(text=f"Fichier sélectionné : {key_file}")
        with open(key_file, 'rb') as file:
            key = file.read()
            # print(f"Clé importée : {key}")


def save_key() -> None:
    n = security_var.get() // 8
    gen_key = al.generate_key(n)
    al.export_file(al.get_path('key file ', '.key'), gen_key)
    print("Clé enregistrée.")


def confirm() -> None:
    global file, key
    if file is not None and key is not None:
        n = len(key) // 2
        rKeys: list[bytes] = al.gen_rKeys(key,'abdelilah',n)
        
        if tab_control.tab(tab_control.select(), "text") == 'Crypter':
            file_en: bytes = al.encrypter_file(file,rKeys,n)
            al.export_file(al.add_tag(file_path),file_en)
            print('file encrypted')
            
        if tab_control.tab(tab_control.select(), "text") == 'Décrypter':
            file_de: bytes = al.decrypter_file(file,rKeys,n)
            al.export_file(al.remove_tag(file_path),file_de)
            print('file decrypted')

        print("Opération confirmée.")


# Création de la fenêtre principale
root = tk.Tk()
root.title("Crypto-Shild")

# Configuration de la géométrie de la fenêtre principale
root.geometry('800x500')  # Taille de la fenêtre ajustée pour l'exemple

# Création des onglets
tab_control = ttk.Notebook(root)

tab1 = tk.Frame(tab_control)
tab2 = tk.Frame(tab_control)

# Widgets pour l'onglet 'Crypter'
security_label = tk.Label(
    tab1, text="Option de Sécurisation pour la génération de la clé :")
security_label.pack(pady=10)

security_var = IntVar(value=128)

radio_128 = Radiobutton(tab1, text="128", variable=security_var, value=128)
radio_192 = Radiobutton(tab1, text="192", variable=security_var, value=192)
radio_256 = Radiobutton(tab1, text="256", variable=security_var, value=256)

radio_128.pack()
radio_192.pack()
radio_256.pack()

security_note = tk.Label(tab1, text="*256 est la clé la plus sécurisée!")
security_note.pack()

save_button = tk.Button(tab1, text="Enregistrer", command=save_key)
save_button.pack(pady=10)

# Widgets pour l'onglet 'Décrypter'
# ...

# Ajout des onglets au contrôle d'onglets
tab_control.add(tab1, text='Crypter')
tab_control.add(tab2, text='Décrypter')

tab_control.pack(expand=1, fill='both')

# Widgets communs
file_label = tk.Label(root, text="Aucun fichier sélectionné",
                      borderwidth=2, relief="sunken", padx=10, pady=5)
file_label.pack(pady=10)

btn_import = tk.Button(root, text="...", command=open_file)
btn_import.pack(pady=10)

key_label = tk.Label(root, text="Importer sa clé :")
key_label.pack(pady=10)

key_label = tk.Label(root, text="Aucun cle sélectionné",
                     borderwidth=2, relief="sunken", padx=10, pady=5)
key_label.pack(pady=10)

import_key_button = tk.Button(root, text="...", command=import_key)
import_key_button.pack(pady=10)

confirm_button = tk.Button(root, text="Confirmer", command=confirm)
confirm_button.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
