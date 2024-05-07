import tkinter as tk
from tkinter import filedialog
import numpy as np

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
def split_by_n(seq, n):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield seq[:n]
        seq = seq[n:]

def to_matrix44(file:np.array):
    list=np.reshape(file,4,4)
    return list


path:str =get_path()
file:str =import_file(path)
file_list: np.array=list(split_by_n(file, 16))
#import the key here


xfile= np.array([]) # declar the arry where we save the result of encreption or decreption 
for i in range(len(file_list)):
    list1: list=list(split_by_n(file_list[i],1))
    list1=np.array(list1)
    try:
        list1= np.reshape(list1,(4,4))
    except:
        list1=np.array(list1)
    #the round shoud start from here


    #to her


    #save the list in xfile 
    xfile=np.append(xfile,list1)

# the last round here


print(xfile)