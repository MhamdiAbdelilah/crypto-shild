import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def open_file():
    file = filedialog.askopenfilename()
    if file:
        # Affiche le nom du fichier sélectionné dans le label
        file_label.config(text= f"Fichier sélectionné : {file}")

def crypter():
    # Ajoutez ici le code pour crypter
    print("Cryptage en cours...")

def decrypter():
    # Ajoutez ici le code pour décrypter
    print("Décryptage en cours...")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Crypto-Shild")

# Conversion de centimètres en pouces, puis en pixels
largeur_cm = 15
hauteur_cm = 15
largeur_px = int((largeur_cm / 2.54) * 96)
hauteur_px = int((hauteur_cm / 2.54) * 96)

# Mise à jour de la géométrie de la fenêtre principale
root.geometry(f'{largeur_px}x{hauteur_px}')

logo = tk.PhotoImage(file='logo.png')
root.iconphoto(False, logo)

# Création des onglets
tab_control = ttk.Notebook(root)

tab1 = tk.Frame(tab_control)
tab2 = tk.Frame(tab_control)

text1_label = tk.Label(root, text="Sélectionner un document : ", relief="flat", padx=10, pady=5)
text1_label.place(x=1, y=35, anchor="nw")

# Label pour afficher le nom du fichier sélectionné
file_label = tk.Label(root, text="Aucun fichier sélectionné", borderwidth=2, relief="sunken", padx=10, pady=5)
file_label.place(x=10, y=70, anchor='nw')  # Place le label en dessous du bouton

# Bouton d'importation de fichier
btn_import = tk.Button(root, text="...", command=open_file)
btn_import.config(width=4, height=1, bd=2)
btn_import.place(relx=0.9, rely=0.146, anchor='center')  # Place le bouton en haut

text2_label = tk.Label(root, text="-----------------------------------------", relief="flat", padx=10, pady=5)
text2_label.place(x=180, y=130, anchor="nw")

text3_label = tk.Label(root, text="Options de sécurisation pour la génération de la clé :", relief="flat", padx=10, pady=5)
text3_label.place(x=1, y=160, anchor="nw")



# Variables pour les boutons radio
option = tk.StringVar(value="none")

# Fonction appelée lorsqu'une option est sélectionnée
def select_option():
    print(f"Option sélectionnée : {option.get()}")

# Création des boutons radio
check1 = tk.Radiobutton(root, text="128", variable=option, value="128", command=select_option)
check1.place(x=50, y=200)

check2 = tk.Radiobutton(root, text="192", variable=option, value="192", command=select_option)
check2.place(x=150, y=200)

check3 = tk.Radiobutton(root, text="256", variable=option, value="256", command=select_option)
check3.place(x=250, y=200)



tab_control.add(tab1, text='Crypter')
tab_control.add(tab2, text='Décrypter')


tab_control.pack(expand=1, fill='both')

root.mainloop()
