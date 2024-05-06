import easygui
from cryptography.fernet import Fernet

# Generate a key and instantiate a Fernet object
key = b'W-B1Mb6hb5hvqvBvwuPcQeAiwp8wzCy2jHTwEiISJZI='
print(f"Generated key: {key}")
f = Fernet(key)

# Function to read file content
def import_file(path):
    with open(path, "rb") as file:  # Open as binary
        return file.read()

# Function to write file content
def export_file(path, content):
    with open(path, "wb") as file:  # Write as binary
        file.write(content)

# Show a file dialog and return the selected file path
selected_file = easygui.fileopenbox()
if selected_file:
    print(f"Selected file: {selected_file}")
    choice = easygui.buttonbox("Choose an action:", choices=["Encrypt", "Decrypt"])
    if choice == "Encrypt":
        try:
            # Encrypt and save the file content
            original_content = import_file(selected_file)
            encrypted_content = f.encrypt(original_content)
            export_file(selected_file, encrypted_content)
            print("File encrypted successfully.")
        except Exception as e:
            print(f"An error occurred during encryption: {e}")
    elif choice == "Decrypt":
        try:
            # Decrypt and save the file content
            encrypted_content = import_file(selected_file)
            decrypted_content = f.decrypt(encrypted_content)
            export_file(selected_file, decrypted_content)
            print("File decrypted successfully.")
        except Exception as e:
            print(f"An error occurred during decryption: {e}")
else:
    print("No file was selected.")
