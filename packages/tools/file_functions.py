import os
from time import sleep

from packages.tools import formatting as f


# Gets folder to sort, returns os.DirEntry object
def get_folder():

    inv_path = True
    while inv_path:
        root_dir = f.surround("-> ", True)

        if root_dir == "test":
            root_dir = 'C:/Users/david/Downloads'

        root_dir = root_dir.replace('"', '')

        try:
            contents_obj = os.scandir(root_dir)
        except:
            print("Invalid path. Try again")
        else:
            inv_path = False

            return contents_obj
        

def get_types(folder_obj):

    types = []

    for file in folder_obj:
        if file.is_file():
            # print(f"Valid file: {file.name}")
            extension = (os.path.splitext(file.name))[1]

            if extension not in types:
                types.append(extension)

    return types

def get_assoc_types(folder_obj):

    valid_files = {}

    for file in folder_obj:
        if file.is_file():
            print(f"Valid file: {file.name}")
            extension = (os.path.splitext(file.name))[1]
            valid_files[file] = extension

    return valid_files
    
