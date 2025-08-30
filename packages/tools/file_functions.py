import os
from time import sleep

from packages.tools import formatting as f


# Gets folder to sort, returns os.DirEntry object and the path of folder
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

            return contents_obj, root_dir
        

def get_types(folder_obj):

    types = {}

    for file in folder_obj:
        if file.is_file(follow_symlinks=False): # Checks if the object is a file

            extension = (os.path.splitext(file.name))[1] # Gets file extension

            if extension not in types:
                types[extension] = 1

            types[extension] += 1

    return types

def get_assoc_types(folder_obj):

    valid_files = {}

    for file in folder_obj:
        if file.is_file():
            print(f"Valid file: {file.name}")
            extension = (os.path.splitext(file.name))[1]
            valid_files[file] = extension

    return valid_files

def mkdir(root_dir, fname="Folder"):

    path_fname = f"{root_dir}/{fname}"

    os.mkdir(path_fname)

    # updated = os.scandir(root_dir)
    # for object in updated:
    #     print(object)

    return "Success"

def get_ext_fullname(extension):

    dict = {
        '.txt':"Plain Text",
        '.docx':"Word Document",
        '.doc':"Word Document",
        '.csv':"Comma-Seperated Values",
        '.pptx':"Powerpoint",
        '.jpg':"JPEG",
        '.png':"Portable Network Graphics",
        '.tiff':"Tag Image File Format",
        '.pdf':"Portable Document Format"
    }

    for ext in dict:
        if ext == extension:
            return dict[ext]
        
        else:
            return None
        

document_extensions = [



    '.docx',
    '.doc',
    '.pdf',
    '.txt',
    '.pptx',
    '.xlsx',
    '.xls'
]

image_extensions = [
    '.jpeg',
    '.png',
    '.webp',
    '.tiff',
]
