import os
from time import sleep

from packages.tools import formatting as f
from packages.tools import file_functions as funcs


options = {
    1:"Default Sort",
    2:"Aggressive Sort",
    3:"Create Custom Sort Profile",
    4:"View description of a sort",
    5:"Exit"
}



def default_sort():

    print("Starting Default Sort...")
    f.line()
    print("Path of directory/folder to sort: ")

    contents, root_dir = funcs.get_folder()


    types = funcs.get_types(contents)
    f.surround(f"Types: {types}")

    types_list = []

    for type in types:
        types_list.append(type)

    print(f"Types List: {types_list}")

    # Sort folder
    for type in types_list:

        # Sort Documents
        if type in funcs.document_extensions:
            
            funcs.gather("Documents", root_dir, contents, type)

        # Sort Images
        if type in funcs.image_extensions:

            funcs.gather("Images", root_dir, contents, type)

        # Sort Audio Files
        if type in funcs.audio_extensions:

            funcs.gather("Audio_Files", root_dir, contents, type)
            
        # Sort Video Files
        if type in funcs.video_extensions:

            funcs.gather("Video_Files", root_dir, contents, type)

        # Sort Program Files
        if type in funcs.application_extensions:

            funcs.gather("Applications", root_dir, contents, type)

    
    funcs.gather("Miscellaneous", root_dir, contents)



def aggressive_sort():







    f.line()


def custom_sort():


    f.line()


def view_desc():

    f.line()