from time import sleep

import shutil
import errno
import json
import stat
import sys
import os

from packages.tools import formatting as f


# Gets folder to sort, returns os.DirEntry object and the path of folder
def get_folder(path="none"):

    inv_path = True
    while inv_path:
        if path == "none":
            root_dir = f.surround("-> ", True)

        else:
            root_dir = path

        files_list = []

        if root_dir == "test":
            root_dir = 'C:/Users/david/Downloads'

        elif root_dir == "huge":
            root_dir = 'C:/Users/david/OneDrive - Norwich University/Misc/Coding/Projects/Sortalicous/Good Test Folder'

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
            else:
                types[extension] += 1

        else:
            if "folder" not in types:
                types["folder"] = 1
            else:
                types["folder"] += 1

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
    except FileExistsError:
        return "Exists"
    except:
        return "Error"
    else:
        return "Success"

# Not tested yet
def move_dir(curr_path, new_path, fname):

    # # Create folder in destination with same name
    # mkdir(new_path, fname)

    new_path = f"{new_path}/{fname}" # Change the new path to include the new folder

    # Copy the contents into the new path
    try:
        shutil.copytree(curr_path, new_path)
    except Exception as oopsie:
        print(oopsie)
        return "Error"

    # Delete the contents of the older folder Recursively?
    try:
        shutil.rmtree(curr_path, ignore_errors=True)
    except Exception as error:
        print(f"Directory Move Error: {error}")

    # Fixes Read Only?
    def errorRemoveReadonly(func, path, excinfo):
        exc_type, exc_value, _ = excinfo
        # Only catch permission denied errors
        if isinstance(exc_value, PermissionError) and exc_value.errno == errno.EACCES:
            os.chmod(path, stat.S_IWRITE)
            func(path)  # retry
        else:
            return


    shutil.rmtree(curr_path, ignore_errors=False, onerror=errorRemoveReadonly)

    try:
        os.rmdir(curr_path)
    except Exception as err:
        # print(f"Directory Delete Error: {err}")
        pass

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
            # Ignore errors lol
            try:
                move_file(f"{root_dir}/{file.name}", f"{root_dir}/{dir_name}")
            except:
                pass

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

def gather_folders(root_dir, contents):
    for thing in contents:
        if (not thing.is_file()) and thing.name not in taken_folder_names:
            exists = mkdir(root_dir, "Folders")
            move_dir(f"{root_dir}/{thing.name}", f"{root_dir}/Folders", thing.name)

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

def get_json(config_name):

    data = "your mom"
    try:
        file = open(f'.\\packages\\startup_configs\\{config_name}', 'r')
    except FileNotFoundError:
        file = open(f"{os.getcwd()}\\Sortalicous\\packages\\startup_configs\\{config_name}", 'r')

    data = json.load(file)
    file.close()
    return data

def overwrite_json(new_json, config_name):

    try:
        file = open(f'.\\packages\\startup_configs\\{config_name}', 'w')
    except FileNotFoundError:
        file = open(f"{os.getcwd()}\\Sortalicous\\packages\\startup_configs\\{config_name}", 'w')
    except Exception as error:
        print(error)
        return "Error"

    json.dump(new_json, file, indent=4)
    file.close()
    return

def make_batch_file(name="default.bat", python_file="startup.py"):
    """
    Creates a batch file that executes the a python script. 

    :param1 name: The name of file
    :param2 python_file: The python script to execute
    :return: The path to the batch file
    """
    
    first_try, second_try = False, False

    # Try to make or open the file
    try:
        file = open(f".\\packages\\batch_files\\{name}", 'w')
        first_try = True
    except FileNotFoundError:
        print("File not found?")
        second_try = True
        file = open(f"{os.getcwd()}\\packages\\batch_files\\{name}", 'w')

    # Get the current directory
    cur_dur = os.getcwd()
     
    # Get the python directory
    python_path = sys.executable

    # Write the commands to the batch file
    file.write(f"cd {cur_dur}\n")
    file.write(f"{python_path} {python_file}")

    # Close it up
    file.close()

    if first_try:
        return f".\\packages\\batch_files\\{name}"
    elif second_try:
        return f"{os.getcwd()}\\packages\\batch_files\\{name}"
    elif not first_try and not second_try:
        return "There was an error with batch file creation"

taken_folder_names = [
    "Documents",
    "Images",
    "Applications",
    "Miscellaneous"
]

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

archive_extensions = [
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
