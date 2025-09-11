import json

from packages.tools import file_functions as funcs
from packages.tools import formatting as f


class Sort_Editor:

    def __init__(self, config_folder_contents):
        self.cfg_contents = config_folder_contents
        
    def view_sorts(self):
        pass

    def create_sort(self):
        
        # --- OUTLINE ---
        # Get the folder to sort
        # Loop:
            # View current contents
            # Add a folder 
            # Specify files to move into that folder
            # Specify files to delete
        # --- OUTLINE ---
        
        f.line()
        print("What would you like to call this sort?")
        name = f.surround("--> ", True)

        cfg_json = {
            "name":name,
            "folders_2_create":[
                {
                    "name":"default"
                }
            ],
            "files_2_delete":[]
        }

        # Get the folder path to sort
        contents, root_dir = funcs.get_folder()
        
        f.surround("Entering Sort Creation Editor . . .")

        creating = True
        while creating:
            print("? for commands")
            f.line()
            usr_inp = input("---> ")

            match usr_inp:

                case "?":
                    show_options()

                case "? -v":
                    show_options(True)

                case "1":
                    print("Please enter the folder name: ")
                    fname = f.surround("----> ")
                    folders = cfg_json["folders_2_create"]
                    folders.append({
                        "name":fname
                    })
            

        def show_options(verbose=False):
            if not verbose:
                print("Commands: ")
                f.line()
                print("1. Make a folder to put things into")
                print("2. Specify what files to move into a folder")
                print("3. Specify file(s) to delete")
                print("4. Specify folder(s) to delete")
                print("E. Exit creation editor")

        pass


    def edit_sort(self):
        pass

    def delete_sort(self):
        pass

    def group_sorts(self):
        pass




    def create_config(self):
        pass




    # Name folders
    # Identify what extensions go in what folders
    # Identify what regex goes in what folders