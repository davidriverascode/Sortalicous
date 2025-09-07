from packages.tools import formatting as f
from packages import options as opts

#! ___________ Outline ___________

#* Sort images - COMPLETED
#* Sort Downloads folder -> installers - COMPLETED
# Run on startup
# Sort documents based off of content?
# Allow user to create custom sorts
# Sort games?
# Multi-thread tasks for faster processing

#! ___________ Outline ___________


def startup(options_dict):

    f.surround("Please choose an option: ")

    for key in options_dict:
        print(f"{key}. {options_dict[key]}")

    user_choice = f.surround("-> ", True)

    if user_choice in options_dict:
        print(f"Selected -> {options_dict[user_choice]}")
    else:
        print(f"Selected -> {user_choice}")
    f.line()

    return execute_selected_option(user_choice, options_dict)


def execute_selected_option(user_choice, options_dict):

    match user_choice:

        case "1":
            opts.default_sort()
            return True

        case "2":
            opts.aggressive_sort()
            return True

        case "3":
            opts.custom_sort()
            return True
        
        case "4":
            opts.view_desc()
            return True
        
        case "5":
            opts.more_options()
            return True
        
        case "E":
            return False



