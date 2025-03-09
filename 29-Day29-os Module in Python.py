import os

def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")

def rename_folder(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"Folder renamed from '{old_name}' to '{new_name}'.")
    except FileNotFoundError:
        print(f"Folder '{old_name}' not found.")

def list_directory(path="."):
    try:
        items = os.listdir(path)
        print(f"Contents of '{path}': {items}")
    except FileNotFoundError:
        print(f"Path '{path}' not found.")

def delete_folder(folder_name):
    try:
        os.rmdir(folder_name)
        print(f"Folder '{folder_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"Folder '{folder_name}' not found.")
    except OSError:
        print(f"Folder '{folder_name}' is not empty or cannot be deleted.")

def get_current_directory():
    print(f"Current Working Directory: {os.getcwd()}")

def change_directory(path):
    try:
        os.chdir(path)
        print(f"Changed directory to '{path}'")
    except FileNotFoundError:
        print(f"Directory '{path}' not found.")

if __name__ == "__main__":
    print("Python OS Module Tutorial")
    get_current_directory()
    create_folder("TestFolder")
    list_directory()
    rename_folder("TestFolder", "RenamedFolder")
    list_directory()
    delete_folder("RenamedFolder")
    list_directory()
