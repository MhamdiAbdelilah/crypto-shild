
import tkinter as tk
from tkinter import filedialog


def import_file(path):
    with open(path, 'rb') as file:  
        return file.read()

def export_file(path:str, content:str):

    #remove extantion
    dot_index = path.rfind('.')
    if dot_index > 0:
        extention:str =path[dot_index:]
        path:str = path[:dot_index]
    else :extention:str=''
    try:
        with open(f'{path}{extention}', "xb") as file: 
                    file.write(content)
                    return print("file saved successfully")
    except:
        # try to save file by changing the name
        for i in range(1,256):
            try :
                with open(f'{path}({i}){extention}', "xb") as file: 
                    file.write(content)
                    return print("file saved successfully")
            except:
                continue
        else: print("Couldn't save the file. All alternative names are taken.")

def add_tag(path):
    path= path +'.ecr'
    return  path

def remove_tag(path):
    if path.endswith('.ecr'):
        path = path[:-4]
    return  path

def get_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    root.destroy()
    return file_path


path: str=get_path()
file: str =import_file(path)+b'encrepted'
export_file(remove_tag(path),file)
print(file)