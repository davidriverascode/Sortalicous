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

    contents = funcs.get_folder()

    f.surround(funcs.get_types(contents))

    # Sort the folder

    # Identify all file types with folder recursively


def aggressive_sort():


    f.line()


def custom_sort():


    f.line()


def view_desc():

    f.line()