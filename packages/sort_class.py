import json
import os

from packages.tools import file_functions as funcs
from packages.tools import formatting as f


class Sort_Editor:

    def __init__(self, config_folder_contents):
        self.cfg_contents = config_folder_contents
        
    def view_sorts(self):
        pass

    def create_sort(self):
        
        #! ___________ Outline ___________
        # Get the folder to sort
        # Loop:
            # View current contents
            # Add a folder 
            # Specify files to move into that folder
            # Specify files to delete
        #! ___________ Outline ___________
        
        f.line()
        print("What would you like to call this sort?")
        name = f.surround("--> ", True)

        # CFG FORMAT FOR VISUALIZATION

        cfg_json = {
            "name":name,
            "folders_2_create":{
                "name":{
                    "extensions":[],
                    "names":[]
                }
            },
            "files_2_delete":[]
        }

        # Get the folder path to sort
        contents, root_dir = funcs.get_folder()
            
        # Create the sort config file
        self.create_config(root_dir, name, cfg_json)
        

        print("? for commands")
        creating = True
        while creating:

            # GRAB THE FRESH CONFIG?

            f.surround("Custom Sort Creation Editor")
            usr_inp = input("---> ")
            f.line()

            if usr_inp == "?":
                self.show_options()
            
            elif usr_inp == "? -v":
                self.show_options(True)

            elif usr_inp == "1" or usr_inp == "folder":
                # Get the folder name
                print("Please enter the folder name: ")
                fname = f.surround("----> ")
                # Add it to the configuration
                folders = cfg_json["folders_2_create"]
                folders["fname"] = {
                    "extensions":[],
                    "names":[]
                }
                f.surround(f"Folder {fname} added.")
                
            elif usr_inp == "2" or usr_inp == "filemove":
                f.surround("What is the name of the folder than you want to move the file into?")
                folder = input("----> ")

                if folder in cfg_json["folders_2_create"]:

                    f.surround("Would you like to identify files by extension, or name?")
                    ident = input("----> ")
                    if ident == "extension":
                        # Monster command that appends the extension to the associated folder
                        (cfg_json["folders_2_create"][folder]["extensions"]).append(f.surround("-----> ", True))
                        pass
                    elif ident == "name":
                        pass
                    else:
                        print("That was not a valid choice. Try again.")

                elif folder not in cfg_json["folders_2_create"]:
                    f.line()
                    print("Invalid folder. Reasons: ")
                    print("    - The folder name was entered incorrectly.")
                    print("    - Folder doesn't exists in the sort config. Please add the folder first.")
                    f.line()

                else:
                    print("Unnexpected error with <filemove> <folder access>")
                    

    def show_options(self, verb=False):
        if verb:
            print("Do verbose output")
            return
        elif not verb:
            print("Commands: ")
            f.line()
            print("1. folder  :  Make a folder to put things into")
            print("2. filemove  :  Specify what files to move into a folder")
            print("3. filedelete  :  Specify file(s) to delete")
            print("4. folderdelete  :  Specify folder(s) to delete")
            print("5. prog  :  View progress")
            print("E. exit  :  Exit creation editor")
            return 
        else:
            print("neither?")
            return


    def edit_sort(self):
        pass

    def delete_sort(self):
        pass

    def group_sorts(self):
        pass




    def create_config(self, path, name, content={"name":"default"}):

        path = f"{os.getcwd()}\\packages\\sorts\\{name}.json"

        # Attempt to create the file
        try:
            file_descriptor = open(path, 'w')
        except FileExistsError:
            return f"File Already Exists: ", path
        except Exception as e:
            return f"Error: {e}"
        
        # Attempt to create the JSON and write to file
        result = funcs.overwrite_json(content, name, path="sorts")

        if result[0] == "Error":
            return result

        return ["Success"]
        
        




    # Name folders
    # Identify what extensions go in what folders
    # Identify what regex goes in what folders