import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


def crypter():
    # Ajoutez ici le code pour crypter
    print("Cryptage en cours...")

def decrypter():
    # Ajoutez ici le code pour décrypter
    print("Décryptage en cours...")
    disable_cryptage_options()

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

tab_control.add(tab1, text='Crypter')
tab_control.add(tab2, text='Décrypter')




text1_label = tk.Label(root, text="Sélectionner un document : ", relief="flat", padx=10, pady=5)
text1_label.place(x=1, y=35, anchor="nw")



def open_file():
    file = filedialog.askopenfilename()
    if file:
        # Affiche le nom du fichier sélectionné dans le label
        file_label.config(text= f"Fichier sélectionné : {file}")

# Label pour afficher le nom du fichier sélectionné
file_label = tk.Label(root, text="Aucun fichier sélectionné", borderwidth=2, relief="sunken", padx=10, pady=5)
file_label.place(x=10, y=70, anchor='nw')  # Place le label en dessous du bouton

# Bouton d'importation de fichier
btn_import = tk.Button(root, text="...", command=open_file)
btn_import.config(width=4, height=1, bd=2)
btn_import.place(relx=0.9, rely=0.150, anchor='center')  # Place le bouton en haut

text2_label = tk.Label(root, text="-----------------------------------------", relief="flat", padx=10, pady=5)
text2_label.place(x=180, y=130, anchor="nw")

text3_label = tk.Label(root, text="Options de sécurisation pour la génération de la clé :", relief="flat", padx=10, pady=5)
text3_label.place(x=1, y=160, anchor="nw")



# Variables pour les boutons check
option = tk.StringVar(value="none")

# Fonction appelée lorsqu'une option est sélectionnée
def select_option():
    print(f"Option sélectionnée : {option.get()}")

# Création des boutons radio
check1 = tk.Radiobutton(root, text="128", variable=option, value="128", command=select_option)
check1.place(x=100, y=200)

check2 = tk.Radiobutton(root, text="192", variable=option, value="192", command=select_option)
check2.place(x=250, y=200)

check3 = tk.Radiobutton(root, text="256", variable=option, value="256", command=select_option)
check3.place(x=400, y=200)


def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file:
        # Ici, vous pouvez ajouter le code pour enregistrer les données dans le fichier sélectionné
        print(f"Fichier enregistré : {file}")

# Bouton de sauvegarde de fichier
btn_save = tk.Button(root, text="Enregistrer", command=save_file)
btn_save.config(width=10, height=1, bd=2)
btn_save.place(x=450, y=250, anchor='nw')  # Place le bouton à l'endroit souhaité

text2_label = tk.Label(root, text="-----------------------------------------", relief="flat", padx=10, pady=5)
text2_label.place(x=180, y=290, anchor="nw")

text4_label = tk.Label(root, text="Importer sa clé : ", relief="flat", padx=10, pady=5)
text4_label.place(x=1, y=320, anchor="nw")

def cle_file():
    file = filedialog.askopenfilename()
    if file:
        # Affiche le nom du fichier sélectionné dans le label
        cle_label.config(text= f"Clé sélectionné : {file}")

# Label pour afficher le nom du fichier sélectionné
cle_label = tk.Label(root, text="Aucune clé sélectionné", borderwidth=2, relief="sunken", padx=10, pady=5)
cle_label.place(x=10, y=360, anchor='nw')  # Place le label en dessous du bouton

cle_import = tk.Button(root, text="...", command=cle_file)
cle_import.config(width=4, height=1, bd=2)
cle_import.place(relx=0.9, rely=0.663, anchor='center')

# Variable globale pour suivre l'état de la clé
cle_importee = False

def cle_file():
    global cle_importee
    file = filedialog.askopenfilename()
    if file:
        cle_label.config(text=f"Clé sélectionnée : {file}")
        cle_importee = True
        update_confirm_button_state()

# Fonction pour mettre à jour l'état du bouton de confirmation
def update_confirm_button_state():
    if cle_importee:
        btn_confirm.config(state="normal")

# Création du bouton de confirmation
btn_confirm = tk.Button(root, text="Confirmer", command=lambda: print("Action confirmée"))
btn_confirm.config(width=10, height=1, bd=2, state="disabled")  # Désactivé par défaut
btn_confirm.place(x=450, y=400, anchor='nw')  # Placez le bouton en bas

# Griser les options de clé de cryptage dans l'onglet de décryptage
def disable_cryptage_options():
    check1.config(state="disabled")
    check2.config(state="disabled")
    check3.config(state="disabled")
    btn_save.config(state="disabled")

# Appeler cette fonction lors de la sélection de l'onglet de décryptage
tab_control.bind("<<NotebookTabChanged>>", disable_cryptage_options)





tab_control.pack(expand=1, fill='both')

root.mainloop()
