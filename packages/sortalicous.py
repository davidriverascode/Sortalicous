from packages.tools import formatting as f
from packages import options as opts

#ANCHOR - Outline
# Sort images
# Sort documents based off of content?
# Run on startup
# Allow user to create custom sorts
# Sort games?
# Sort Downloads folder -> installers
# Multi-thread tasks for faster processing


def startup(options_dict):

    f.surround("Hello, welcome to Sortalicous!!")

    f.surround("Please choose an option: ")

    for key in options_dict:
        print(f"{key}. {options_dict[key]}")

    user_choice = f.surround("-> ", True)

    print(options_dict[int(user_choice)])
    f.line()

    return execute_selected_option(user_choice, options_dict)


def execute_selected_option(user_choice, options_dict):

    user_choice = int(user_choice)

    if user_choice == 5:
        return False

    match user_choice:

        case 1:
            opts.default_sort()
            return True

        case 2:
            opts.aggressive_sort()
            return True

        case 3:
            opts.custom_sort()
            return True
        case 4:
            opts.view_desc()
            return True




