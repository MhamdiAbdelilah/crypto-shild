import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


# Partie correspondant à l'onglet "Crypter"
def onglet_crypter(tab):
    text1_label = tk.Label(tab, text="Sélectionner un document à crypter : ", relief="flat", padx=10, pady=5)
    text1_label.place(x=1, y=35)

    def choisir_file():
        file = filedialog.askopenfilename()
        if file:
            file_label.config(text=f"Fichier sélectionné : {file}")


    file_label = tk.Label(tab, text="Aucun fichier sélectionné", borderwidth=2, relief="sunken", padx=10, pady=5)
    file_label.place(x=10, y=70)

    # Bouton d'importation de fichier
    btn_import = tk.Button(tab, text="...", command=choisir_file)
    btn_import.config(width=4, height=1, bd=2, cursor="hand2", overrelief="solid")
    btn_import.place(relx=0.86, rely=0.132)

    text2_label = tk.Label(tab, text="-----------------------------------------", relief="flat", padx=10, pady=5)
    text2_label.place(x=180, y=130)

    text3_label = tk.Label(tab, text="Options de sécurisation pour la génération de la clé :", relief="flat", padx=10, pady=5)
    text3_label.place(x=1, y=160)

    # Variables pour les boutons check
    option = tk.StringVar(value="none")

 
    def select_option():
        print(f"Option sélectionnée : {option.get()}")


    check1 = tk.Radiobutton(tab, text="128", variable=option, value="128", command=select_option)
    check1.place(x=100, y=200)

    check2 = tk.Radiobutton(tab, text="192", variable=option, value="192", command=select_option)
    check2.place(x=250, y=200)

    check3 = tk.Radiobutton(tab, text="256", variable=option, value="256", command=select_option)
    check3.place(x=400, y=200)

    def save_file():
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file:
            save_file.config(text=f"Fichier enregistré : {file}")
            print(f"Fichier enregistré : {file}")

    # Bouton de sauvegarde de fichier
    btn_save = tk.Button(tab, text="Enregistrer", command=save_file)
    btn_save.config(width=10, height=1, bd=2, cursor="hand2", overrelief="solid")
    btn_save.place(x=450, y=255)

    save_file = tk.Label(tab, text="Ancun enregistré", borderwidth=2, relief="sunken", padx=10, pady=5)
    save_file.place(x=10, y=255)

    text2_label = tk.Label(tab, text="-----------------------------------------", relief="flat", padx=10, pady=5)
    text2_label.place(x=180, y=290)

    text4_label = tk.Label(tab, text="Importer sa clé : ", relief="flat", padx=10, pady=5)
    text4_label.place(x=1, y=320)

    def cle_file():
        file = filedialog.askopenfilename()
        if file:
            cle_label.config(text=f"Clé sélectionnée : {file}")


    cle_label = tk.Label(tab, text="Aucune clé sélectionnée", borderwidth=2, relief="sunken", padx=10, pady=5)
    cle_label.place(x=10, y=360)

    cle_import = tk.Button(tab, text="...", command=cle_file)
    cle_import.config(width=4, height=1, bd=2, cursor="hand2", overrelief="solid")
    cle_import.place(relx=0.86, rely=0.668)

    # Bouton confirmer
    btn_confirmer = tk.Button(tab, text="Confirmer", command=None)
    btn_confirmer.config(width=10, height=1, bd=2, cursor="hand2", overrelief="solid")
    btn_confirmer.place(x=250, y=480)













# l'onglet "Décrypter"
def onglet_decrypter(tab):
    text1_label = tk.Label(tab, text="Sélectionner un document à décrypter : ", relief="flat", padx=10, pady=5)
    text1_label.place(x=1, y=35)

    def choisir_file():
        file = filedialog.askopenfilename()
        if file:
            file_label.config(text=f"Fichier sélectionné : {file}")


    file_label = tk.Label(tab, text="Aucun fichier sélectionné", borderwidth=2, relief="sunken", padx=10, pady=5)
    file_label.place(x=10, y=70)


    btn_import = tk.Button(tab, text="...", command=choisir_file)
    btn_import.config(width=4, height=1, bd=2, cursor="hand2", overrelief="solid")
    btn_import.place(relx=0.86, rely=0.132)

    text2_label = tk.Label(tab, text="-----------------------------------------", relief="flat", padx=10, pady=5)
    text2_label.place(x=180, y=130)

    text3_label = tk.Label(tab, text="Options de sécurisation pour la génération de la clé :", relief="flat", padx=10, pady=5)
    text3_label.place(x=1, y=160)

    # Variables pour les boutons check
    option = tk.StringVar(value="none")

  
    def select_option():
        print(f"Option sélectionnée : {option.get()}")

    check1 = tk.Radiobutton(tab, text="128", variable=option, value="128", command=select_option)
    check1.place(x=100, y=200)
    check2 = tk.Radiobutton(tab, text="192", variable=option, value="192", command=select_option)
    check2.place(x=250, y=200)
    check3 = tk.Radiobutton(tab, text="256", variable=option, value="256", command=select_option)
    check3.place(x=400, y=200)


    def save_file():
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file:
            # ajouter le code pour enregistrer les données dans le fichier sélectionné
            print(f"Le fichier est enregistré dans : {file}")

    # Bouton de sauvegarde de fichier
    btn_save = tk.Button(tab, text="Enregistrer", command=save_file)
    btn_save.config(width=10, height=1, bd=2)
    btn_save.place(x=450, y=250)

    text2_label = tk.Label(tab, text="-----------------------------------------", relief="flat", padx=10, pady=5)
    text2_label.place(x=180, y=290)

    text4_label = tk.Label(tab, text="Importer sa clé : ", relief="flat", padx=10, pady=5)
    text4_label.place(x=1, y=320)

    

    def cle():
        file = filedialog.askopenfilename()
        if file:
            cle_label.config(text=f"Clé sélectionnée : {file}")


    cle_label = tk.Label(tab, text="Aucune clé sélectionnée", borderwidth=2, relief="sunken", padx=10, pady=5)
    cle_label.place(x=10, y=360)

    cle_import = tk.Button(tab, text="...", command=cle)
    cle_import.config(width=4, height=1, bd=2, cursor="hand2", overrelief="solid")
    cle_import.place(relx=0.86, rely=0.668)

    btn_confirmer = tk.Button(tab, text="Confirmer", command=None)
    btn_confirmer.config(width=10, height=1, bd=2, cursor="hand2", overrelief="solid")
    btn_confirmer.place(x=250, y=480)


    # Griser les options
    def desactiver_options():
        check1.config(state="disabled")
        check2.config(state="disabled")
        check3.config(state="disabled")
        btn_save.config(state="disabled")


    desactiver_options()










# Création de la fenêtre principale
interface = tk.Tk()
interface.title("Crypto-Shild")
logo = tk.PhotoImage(file='logo.png')
interface.iconphoto(False, logo)
interface.resizable(False, False)

# Taille de la fenêtre
largeur_cm = 15
hauter_cm = 15
largeur_px = int((largeur_cm / 2.54) * 96)
hauteur_px = int((largeur_cm / 2.54) * 96)
interface.geometry(f"{largeur_px}x{largeur_px}")


# Création des onglets
tab_control = ttk.Notebook(interface)

tab1 = tk.Frame(tab_control)
tab2 = tk.Frame(tab_control)

tab_control.add(tab1, text='Crypter')
tab_control.add(tab2, text='Décrypter')


onglet_crypter(tab1)
onglet_decrypter(tab2)

tab_control.pack(expand=1, fill='both')

interface.mainloop()
