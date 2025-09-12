from time import sleep
import subprocess
import os

from packages.tools import formatting as f
from packages.tools import file_functions as funcs
from packages import sort_class as sort


options = {
    "1":"Default Sort",
    "2":"Aggressive Sort",
    "3":"Create Custom Sort Profile",
    "4":"View description of a sort",
    "5":"More Options",
    "E":"Exit"
}


def default_sort(sort_path="default", auto=False):

    if auto:
        f.print_random_title()
        f.line()

    print("Starting Default Sort...")
    f.line()

    # Determine if path to sort was passed
    if sort_path == "default":
        contents, root_dir = funcs.get_folder()
    else:
        contents, root_dir = funcs.get_folder(sort_path)

    funcs.gather_folders(root_dir, contents)

    types = funcs.get_types(contents)

    types_list = []

    for type in types:
        types_list.append(type)

    print("Sorting . . .")

    # Sort folder
    for type in types_list:

        # if type == "folder":
            # move the folders

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

        # Sort Archives
        if type in funcs.archive_extensions:

            funcs.gather("Archives", root_dir, contents, type)
    
    funcs.gather("Miscellaneous", root_dir, contents)
    
    f.line()
    print("Finished Sort. Check folder to see!")

def aggressive_sort():

    print("Feature not finished, check back another day!")

def custom_sort():

    print("WARNING - FEATURE UNDER DEVELOPMENT")

    config_folder_contents, root_dir = funcs.get_folder(f".\\packages\\sorts")

    custom_sort = sort.Sort_Editor(config_folder_contents)

    f.surround("Entering Custom Sort Creation Editor . . .")

    custom_sort.create_sort()


def view_desc():

    print("\n1. Default Sort")
    print("\n    - Sorts items into folders according to the extension. For example, will sort .docx (Word Documents) into a folder called 'Documents'")
    print("\n2. Aggressive Sort")
    print("\n    - Sorts items into folders according to the extension. Then sorts then into further folder alphabetically based off the file name.")
    print("\n3. Create Custom Sort Profile")
    print("\n    - Allows the user to create custom sort profiles. Takes a little bit of time to set up, but makes the sort more personalized\n")

def more_options():

    print("More Options")
    f.line()
    print("1. Run a sort on startup")
    print("2. Run a sort on a time interval")
    answer = f.surround("-> ", True)

    match answer:

        case "1": # RUN ON STARTUP OPTION

            # Make the batch file that will run the python script
            funcs.make_batch_file()

            # Get the default sort config for schtasks.exe
            config = funcs.get_json("default.json")

            # Edit the default sort config
            config["startup"] = True

            command = config["command"]
            command["/tr"] = f'"{os.getcwd()}\\packages\\batch_files\default.bat"'
            config["command"] = command
                
            path_to_sort = f.surround("Path to sort: ", True)
            config["sort-path"] = path_to_sort
            
            funcs.overwrite_json(config, "default.json")

            # Re-fetch the config json after editing it 
            updated_config = (funcs.get_json("default.json"))["command"]

            # Craft the final schtasks.exe command
            final_command = ""
            for key in updated_config:
                final_command = final_command + f"{key} {updated_config[key]} "

            # And then try and run it
            try:
                subprocess.call(final_command, shell=True)
            except Exception as e:
                print(f"\nError: {e}\n")
                input("Press any key to exit -> ")

            

            