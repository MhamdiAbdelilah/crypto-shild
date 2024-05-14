import tkinter as tk
from tkinter import messagebox
import algothme as al
from tkinter import filedialog, ttk, Radiobutton, IntVar


# Variables

file_crypt = "Aucun fichier sélectionné"
file_decrypt = "Aucun fichier sélectionné"
key_file = "Aucun fichier sélectionné"
key_path = ""


# Fonction

def open_file() -> None:
    global file,file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        file_label.config(text=f"Fichier sélectionné : {file_path}")
        with open(file_path, 'rb') as file:
            file = file.read()
            print(f"file importée : {file}")


def import_key() -> None:
    global key, key_label, key_file
    key_file = filedialog.askopenfilename(filetypes=[("Key Files", "*.key")])
    if key_file:
        key_label.config(text=f"Fichier sélectionné : {key_file}")
        with open(key_file, 'rb') as file:
            key = file.read()
            print(f"Clé importée : {key}")


def save_key() -> None:
    global option
    n = option.get() // 8
    gen_key = al.generate_key(n)
    key_path = al.get_path('key file ', '.key')
    al.export_file(key_path , gen_key)
    save_file.config(text=f"Cle enregistrée dans:    {key_path}")
    print("Clé enregistrée.")
    messagebox.showinfo("Information", "Clé enregistrée")
    


def confirm() -> None:
    global file, key
    if file is not None and key is not None:
        n = len(key) // 2
        rKeys: list[bytes] = al.gen_rKeys(key,'abdelilah',n)
        
        if onglets.tab(onglets.select(), "text") == 'Crypter':
            file_en: bytes = al.encrypter_file(file,rKeys,n)
            al.export_file(file_path,file_en)
            print('file encrypted')
            messagebox.showinfo("Information", "Fichier Crypter")
            
        if onglets.tab(onglets.select(), "text") == 'Décrypter':
            file_de: bytes = al.decrypter_file(file,rKeys,n)
            al.export_file(file_path,file_de)
            print('file decrypted')
            messagebox.showinfo("Information", "Fichier Décrypter")
            

        print("Opération confirmée.")



def onglet_crypter(tab):
    global file_label, text3_label, option, key_label, save_file, path_key, key_path

    text1_label = tk.Label(tab, text="Sélectionner un document à crypter : ", relief="flat", padx=10, pady=5)
    text1_label.place(x=1, y=20)

    file_label = tk.Label(tab, width=60, text=f"Fichier sélectionné : {file_crypt}", borderwidth=2, relief="sunken", padx=10, pady=5, anchor="w")
    file_label.place(x=10, y=60)

    # Bouton d'importation de fichier
    btn_import = tk.Button(tab, text="...", command=open_file)
    btn_import.config(width=4, height=1, bd=2, cursor="hand2", overrelief="solid")
    btn_import.place(relx=0.86, rely=0.113)

    text2_label = tk.Label(tab, text="-----------------------------------------", relief="flat", padx=10, pady=5)
    text2_label.place(x=170, y=116)

    text3_label = tk.Label(tab, text="Options de sécurisation pour la génération de la clé :", relief="flat", padx=10, pady=5)
    text3_label.place(x=1, y=160)

    # Variables pour les boutons check
    option = tk.IntVar(value=128)



    check1 = tk.Radiobutton(tab, text="Faible (128)", variable=option, value=128)
    check1.place(x=100, y=200)

    check2 = tk.Radiobutton(tab, text="Moyen (192)", variable=option, value=192)
    check2.place(x=250, y=200)

    check3 = tk.Radiobutton(tab, text="Fort (256)", variable=option, value=256)
    check3.place(x=400, y=200)


    # Bouton de sauvegarde de fichier
    btn_save = tk.Button(tab, text="Enregistrer", command=save_key, wraplength=300, justify='left')
    btn_save.config(width=10, height=1, bd=2, cursor="hand2", overrelief="solid")
    btn_save.place(x=450, y=255)

    save_file = tk.Label(tab, width=55, text=f"Clé enregistrée dans : {key_path}", borderwidth=2, relief="sunken", padx=10, pady=5, anchor="w")
    save_file.place(x=10, y=255)

    text2_label = tk.Label(tab, text="-----------------------------------------", relief="flat", padx=10, pady=5)
    text2_label.place(x=170, y=310)

    text4_label = tk.Label(tab, text="Importer sa clé :", relief="flat", padx=10, pady=5)
    text4_label.place(x=1, y=350)



    key_label = tk.Label(tab, width=60, text=f"Fichier sélectionné : {key_file}", borderwidth=2, relief="sunken", padx=10, pady=5, anchor="w")
    key_label.place(x=10, y=390)

    cle_import = tk.Button(tab, text="...", command=import_key)
    cle_import.config(width=4, height=1, bd=2, cursor="hand2", overrelief="solid")
    cle_import.place(relx=0.86, rely=0.723)

    # Bouton confirmer
    btn_confirmer = tk.Button(tab, text="Confirmer", command=confirm)
    btn_confirmer.config(width=10, height=1, bd=2, cursor="hand2", overrelief="solid")
    btn_confirmer.place(x=240, y=480)







# l'onglet "Décrypter"
def onglet_decrypter(tab):
    global file_label, text3_label, option, key_label, save_file

    text1_label = tk.Label(tab, text="Sélectionner un document à décrypter : ", relief="flat", padx=10, pady=5)
    text1_label.place(x=1, y=20)



    file_label = tk.Label(tab, width=60, text=f"Fichier sélectionné : {file_decrypt}", borderwidth=2, relief="sunken", padx=10, pady=5, anchor="w")
    file_label.place(x=10, y=60)


    btn_import = tk.Button(tab, text="...", command=open_file)
    btn_import.config(width=4, height=1, bd=2, cursor="hand2", overrelief="solid")
    btn_import.place(relx=0.86, rely=0.113)

    text2_label = tk.Label(tab, text="-----------------------------------------", relief="flat", padx=10, pady=5)
    text2_label.place(x=170, y=116)

    text3_label = tk.Label(tab, text="Options de sécurisation pour la génération de la clé :", relief="flat", padx=10, pady=5)
    text3_label.place(x=1, y=160)

    # Variables pour les boutons check
    option = tk.StringVar(value="none")

  

    check1 = tk.Radiobutton(tab, text="Fort (128)", variable=option, value="128",)
    check1.place(x=100, y=200)
    check2 = tk.Radiobutton(tab, text="Moyen (192)", variable=option, value="192",)
    check2.place(x=250, y=200)
    check3 = tk.Radiobutton(tab, text="Fort (256)", variable=option, value="256",)
    check3.place(x=400, y=200)


    # Bouton de sauvegarde de fichier
    btn_save = tk.Button(tab, text="Enregistrer" )
    btn_save.config(width=10, height=1, bd=2)
    btn_save.place(x=450, y=255)

    text2_label = tk.Label(tab, text="-----------------------------------------", relief="flat", padx=10, pady=5)
    text2_label.place(x=170, y=310)

    text4_label = tk.Label(tab, text="Importer sa clé : ", relief="flat", padx=10, pady=5)
    text4_label.place(x=1, y=350)



    key_label = tk.Label(tab, width=60, text=f"Fichier sélectionné : {key_file}", borderwidth=2, relief="sunken", padx=10, pady=5, anchor="w")
    key_label.place(x=10, y=390)

    cle_import = tk.Button(tab, text="...", command=import_key)
    cle_import.config(width=4, height=1, bd=2, cursor="hand2", overrelief="solid")
    cle_import.place(relx=0.86, rely=0.723)

    btn_confirmer = tk.Button(tab, text="Confirmer", command=confirm )
    btn_confirmer.config(width=10, height=1, bd=2, cursor="hand2", overrelief="solid")
    btn_confirmer.place(x=240, y=480)
    

    # Griser les options
    check1.config(state="disabled")
    check2.config(state="disabled")
    check3.config(state="disabled")
    btn_save.config(state="disabled")




def onglet_a_propos(tab):
    for i in tab.winfo_children():
        i.destroy()
    texte_a_propos = """
    Crypto-Shild

    Version 1.0

    Développé par ABDELILAH (Patron) - LAKSHAN - BILAL

    Crypto-Shild est une application de cryptage et de décryptage de fichiers 
    basée sur des algorithmes de chiffrement robustes. POUR VOUS LES AMIS !

    Pour plus d'informations, veuillez contacter crpto-shiel@aide.com
    """

    texte_propos1 = tk.Label(tab, text=texte_a_propos, relief="flat", justify="left")
    texte_propos1.pack(fill="both", expand=True)




def onglet_aide(tab):
    for i in tab.winfo_children():
        i.destroy()
    texte_aide = """
    Bienvenue dans Crypto-Shild !

    Ce logiciel vous permet de crypter et de décrypter des fichiers en toute sécurité 
    à l'aide d'algorithmes de chiffrement robustes.

    Pour crypter un fichier :
    1. Sélectionnez l'onglet "Crypter".
    2. Cliquez sur le bouton "..." pour choisir le fichier que vous souhaitez crypter.
    3. Choisissez le niveau de sécurité pour la génération de la clé.
    4. Cliquez sur le bouton "Enregistrer" pour sauvegarder la clé générée.
    5. Importez votre clé en cliquant sur le bouton "..." et en sélectionnant le fichier contenant la clé.
    6. Cliquez sur le bouton "Confirmer" pour crypter le fichier sélectionné.

    Pour décrypter un fichier :
    1. Sélectionnez l'onglet "Décrypter".
    2. Cliquez sur le bouton "..." pour choisir le fichier que vous souhaitez décrypter.
    3. Choisissez le niveau de sécurité pour la génération de la clé. (Si vous avez la clé, sinon cela sera 
    désactivé)
    4. Importez votre clé en cliquant sur le bouton "..." et en sélectionnant le fichier contenant la clé.
    5. Cliquez sur le bouton "Confirmer" pour décrypter le fichier sélectionné.

    C'est tout ! Vous pouvez maintenant crypter et décrypter 
    vos fichiers en toute sécurité avec Crypto-Shild.
    """

    texte_aide1 = tk.Label(tab, text=texte_aide, relief="flat", padx=10, pady=5, justify="left")
    texte_aide1.pack(fill="both", expand=True)








# Création de la fenêtre principale
interface = tk.Tk()
interface.title("Crypto-Shild")
# logo = tk.PhotoImage(file='icon.ico')
# interface.iconphoto(False, logo)
# interface.resizable(False, False)

# Taille de la fenêtre
largeur_cm = 15
hauter_cm = 15
largeur_px = int((largeur_cm / 2.54) * 96)
hauteur_px = int((largeur_cm / 2.54) * 96)
interface.geometry(f"{largeur_px}x{largeur_px}")


# Création des onglets
onglets = ttk.Notebook(interface)

onglet1 = tk.Frame(onglets)
onglet2 = tk.Frame(onglets)
onglet3 = tk.Frame(onglets)
onglet4 = tk.Frame(onglets)

onglets.add(onglet1, text='Crypter')
onglets.add(onglet2, text='Décrypter')
onglets.add(onglet3, text='A propos')
onglets.add(onglet4, text='Aide')



def on_tab_changed(event):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")

    if tab_text == 'Crypter':
        onglet_crypter(onglet1)
    elif tab_text == 'Décrypter':
        onglet_decrypter(onglet2)
    elif tab_text == 'A propos' :    
        onglet_a_propos(onglet3)
    elif tab_text == 'Aide':
        onglet_aide(onglet4)
    
onglets.bind('<<NotebookTabChanged>>', on_tab_changed)
onglets.pack(expand=1, fill='both')

interface.mainloop()