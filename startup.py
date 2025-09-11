try:
    from packages import options as opts
    from packages.tools import file_functions as funcs
except:
    print("Error")
    input("-> ")
    
def main():
    # Get the sort path from the configuration
    config = funcs.get_json("default.json")
    path = config["sort-path"]

    # Run the default sort
    opts.default_sort(path, True)
    input("\n\nPress any key to exit -> ")

if __name__ == '__main__':
    main()