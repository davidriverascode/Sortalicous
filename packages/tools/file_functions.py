import shutil
import os
from time import sleep

from packages.tools import formatting as f


# Gets folder to sort, returns os.DirEntry object and the path of folder
def get_folder():

    inv_path = True
    while inv_path:
        root_dir = f.surround("-> ", True)

        files_list = []

        if root_dir == "test":
            root_dir = 'C:/Users/david/Downloads'

        root_dir = root_dir.replace('"', '')

        try:
            contents_obj = os.scandir(root_dir)
        except:
            print("Invalid path. Try again")
        else:
            inv_path = False

            for file in contents_obj:
                files_list.append(file)

            return files_list, root_dir
        

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
        if file.is_file(follow_symlinks=False):
            extension = (os.path.splitext(file.name))[1]
            valid_files[file] = extension

    return valid_files

def mkdir(root_dir, fname="Folder"):

    path_fname = f"{root_dir}/{fname}"

    try:
        os.mkdir(path_fname)
    except:
        return "Error"
    else:
        return "Success"

# Not tested yet
def move_dir(curr_path, new_path, fname):

    # Create folder in destination with same name
    mkdir(new_path, fname)

    new_path = f"{new_path}/{fname}" # Change the new path to include the new folder

    # Copy the contents into the new path
    shutil.copytree(curr_path, new_path)

# Will override existing files
def move_file(file_path, destination):

    new_path = shutil.move(file_path, destination)



    return new_path

def gather(dir_name, root_dir, contents, type="Any"):

    if type == "Any":
          
        # Make directory
        try:
            mkdir(root_dir, dir_name)
        except:
            pass

        # Move the files
        assoc_types = get_assoc_types(contents)
        for file in assoc_types:
            try:
                move_file(f"{root_dir}/{file.name}", f"{root_dir}/{dir_name}")
            except Exception as e:
                print(f"File move failure-> {e}")

        return
    
    # Make directory
    try:
        mkdir(root_dir, dir_name)
    except:
        pass

    # Move the files
    assoc_types = get_assoc_types(contents)
    for file in assoc_types:
        if assoc_types[file] == type:
            try:
                move_file(f"{root_dir}/{file.name}", f"{root_dir}/{dir_name}")
            except Exception as e:
                print(f"File move failure: {e}")

    return

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
    '.xls',
    '.dta',
    '.rtf',
    '.csv',
    '.wps',
    '.msg',
    '.wpd'
]

image_extensions = [
    '.jpeg',
    '.jpg',
    '.png',
    '.webp',
    '.tiff',
    '.tif',
    '.bmp',
    '.eps'
]

application_extensions = [
    '.exe',
    '.c',
    '.cpp',
    '.java',
    '.py',
    '.js',
    '.ts',
    '.cs',
    '.swift',
    '.pl',
    '.sh',
    '.bat',
    '.com'
]

audio_extensions = [
    '.mp3',
    '.wma',
    '.snd',
    '.wav',
    '.ra',
    '.au',
    '.aac'
]

video_extensions = [
    '.mp4',
    '.3gp',
    '.avi',
    '.mpg',
    '.mov',
    '.wmv'
]

compressed_extensions = [
    '.rar',
    '.zip',
    '.hqx',
    '.arj',
    '.tar',
    '.arc',
    '.sit',
    '.gz',
    '.z'
]

webpage_extensions = [
    '.html',
    '.htm',
    '.xhtml',
    '.asp',
    '.css',
    '.aspx',
    '.rss',
    '.php'
]
