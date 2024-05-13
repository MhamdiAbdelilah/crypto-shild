import tkinter as tk
from tkinter import messagebox
import algothme as al
from tkinter import filedialog, ttk, Radiobutton, IntVar

file_path = "Aucun fichier sélectionné"
path_key = "Importer sa clé : "

def open_file() -> None:
    global file,file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        file_label.config(text=f"Fichier sélectionné : {file_path}")
        with open(file_path, 'rb') as file:
            file = file.read()
            # print(f"file importée : {file}")


def import_key() -> None:
    global key, key_label
    key_file = filedialog.askopenfilename(filetypes=[("Key Files", "*.key")])
    if key_file:
        key_label.config(text=f"Fichier sélectionné : {key_file}")
        with open(key_file, 'rb') as file:
            key = file.read()
            # print(f"Clé importée : {key}")


def save_key() -> None:
    global option
    n = option.get() // 8
    gen_key = al.generate_key(n)
    key_path = al.get_path('key file ', '.key')
    al.export_file(key_path , gen_key)
    save_file.config(text=f"Fichier sélectionné : {key_path}")
    print("Clé enregistrée.")
    messagebox.showinfo("Information", "Clé enregistrée")
    


def confirm() -> None:
    global file, key
    if file is not None and key is not None:
        n = len(key) // 2
        rKeys: list[bytes] = al.gen_rKeys(key,'abdelilah',n)
        
        if tab_control.tab(tab_control.select(), "text") == 'Crypter':
            file_en: bytes = al.encrypter_file(file,rKeys,n)
            al.export_file(al.add_tag(file_path),file_en)
            print('file encrypted')
            messagebox.showinfo("Information", "file encrypted")
            
        if tab_control.tab(tab_control.select(), "text") == 'Décrypter':
            file_de: bytes = al.decrypter_file(file,rKeys,n)
            al.export_file(al.remove_tag(file_path),file_de)
            print('file decrypted')
            messagebox.showinfo("Information", "file decrypted")
            

        print("Opération confirmée.")

def onglet_crypter(tab):
    global file_label, text3_label, option, key_label, save_file, path_key

    text1_label = tk.Label(tab, text="Sélectionner un document à crypter : ", relief="flat", padx=10, pady=5)
    text1_label.place(x=1, y=35)

    file_label = tk.Label(tab, text=file_path, borderwidth=2, relief="sunken", padx=10, pady=5)
    file_label.place(x=10, y=70)

    # Bouton d'importation de fichier
    btn_import = tk.Button(tab, text="...", command=open_file)
    btn_import.config(width=4, height=1, bd=2, cursor="hand2", overrelief="solid")
    btn_import.place(relx=0.86, rely=0.132)

    text2_label = tk.Label(tab, text="-----------------------------------------", relief="flat", padx=10, pady=5)
    text2_label.place(x=180, y=130)

    text3_label = tk.Label(tab, text="Options de sécurisation pour la génération de la clé :", relief="flat", padx=10, pady=5)
    text3_label.place(x=1, y=160)

    # Variables pour les boutons check
    option = tk.IntVar(value=128)



    check1 = tk.Radiobutton(tab, text="128", variable=option, value=128)
    check1.place(x=100, y=200)

    check2 = tk.Radiobutton(tab, text="192", variable=option, value=192)
    check2.place(x=250, y=200)

    check3 = tk.Radiobutton(tab, text="256", variable=option, value=256)
    check3.place(x=400, y=200)


    # Bouton de sauvegarde de fichier
    btn_save = tk.Button(tab, text="Enregistrer", command=save_key)
    btn_save.config(width=10, height=1, bd=2, cursor="hand2", overrelief="solid")
    btn_save.place(x=450, y=255)

    save_file = tk.Label(tab, text="Ancun enregistré", borderwidth=2, relief="sunken", padx=10, pady=5)
    save_file.place(x=10, y=255)

    text2_label = tk.Label(tab, text="-----------------------------------------", relief="flat", padx=10, pady=5)
    text2_label.place(x=180, y=290)

    text4_label = tk.Label(tab, text=path_key, relief="flat", padx=10, pady=5)
    text4_label.place(x=1, y=320)



    key_label = tk.Label(tab, text="Aucune clé sélectionnée", borderwidth=2, relief="sunken", padx=10, pady=5)
    key_label.place(x=10, y=360)

    cle_import = tk.Button(tab, text="...", command=import_key)
    cle_import.config(width=4, height=1, bd=2, cursor="hand2", overrelief="solid")
    cle_import.place(relx=0.86, rely=0.668)

    # Bouton confirmer
    btn_confirmer = tk.Button(tab, text="Confirmer", command=confirm)
    btn_confirmer.config(width=10, height=1, bd=2, cursor="hand2", overrelief="solid")
    btn_confirmer.place(x=250, y=480)


# l'onglet "Décrypter"
def onglet_decrypter(tab):
    global file_label, text3_label, option, key_label, save_file
    text1_label = tk.Label(tab, text="Sélectionner un document à décrypter : ", relief="flat", padx=10, pady=5)
    text1_label.place(x=1, y=35)



    file_label = tk.Label(tab, text=file_path, borderwidth=2, relief="sunken", padx=10, pady=5)
    file_label.place(x=10, y=70)


    btn_import = tk.Button(tab, text="...", command=open_file)
    btn_import.config(width=4, height=1, bd=2, cursor="hand2", overrelief="solid")
    btn_import.place(relx=0.86, rely=0.132)

    text2_label = tk.Label(tab, text="-----------------------------------------", relief="flat", padx=10, pady=5)
    text2_label.place(x=180, y=130)

    text3_label = tk.Label(tab, text="Options de sécurisation pour la génération de la clé :", relief="flat", padx=10, pady=5)
    text3_label.place(x=1, y=160)

    # Variables pour les boutons check
    option = tk.StringVar(value="none")

  

    check1 = tk.Radiobutton(tab, text="128", variable=option, value="128",)
    check1.place(x=100, y=200)
    check2 = tk.Radiobutton(tab, text="192", variable=option, value="192",)
    check2.place(x=250, y=200)
    check3 = tk.Radiobutton(tab, text="256", variable=option, value="256",)
    check3.place(x=400, y=200)


    # Bouton de sauvegarde de fichier
    btn_save = tk.Button(tab, text="Enregistrer" )
    btn_save.config(width=10, height=1, bd=2)
    btn_save.place(x=450, y=250)

    text2_label = tk.Label(tab, text="-----------------------------------------", relief="flat", padx=10, pady=5)
    text2_label.place(x=180, y=290)

    text4_label = tk.Label(tab, text="Importer sa clé : ", relief="flat", padx=10, pady=5)
    text4_label.place(x=1, y=320)




    key_label = tk.Label(tab, text="Aucune clé sélectionnée", borderwidth=2, relief="sunken", padx=10, pady=5)
    key_label.place(x=10, y=360)

    cle_import = tk.Button(tab, text="...", command=import_key)
    cle_import.config(width=4, height=1, bd=2, cursor="hand2", overrelief="solid")
    cle_import.place(relx=0.86, rely=0.668)

    btn_confirmer = tk.Button(tab, text="Confirmer", command=confirm)
    btn_confirmer.config(width=10, height=1, bd=2, cursor="hand2", overrelief="solid")
    btn_confirmer.place(x=250, y=480)


    # Griser les options
    check1.config(state="disabled")
    check2.config(state="disabled")
    check3.config(state="disabled")
    btn_save.config(state="disabled")




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

def on_tab_changed(event):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")

    if tab_text == 'Crypter':
        onglet_crypter(tab1)
    elif tab_text == 'Décrypter':
        onglet_decrypter(tab2)

tab_control.bind('<<NotebookTabChanged>>', on_tab_changed)
tab_control.pack(expand=1, fill='both')

interface.mainloop()