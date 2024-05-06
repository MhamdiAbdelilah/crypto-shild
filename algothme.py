import easygui
selected_file = easygui.fileopenbox()  # Show a file dialog and return the selected file path
print(selected_file)

path = "./test.txt"
def import_file(path):
    list = open(path, "r").read()
    return list

print(import_file(selected_file))