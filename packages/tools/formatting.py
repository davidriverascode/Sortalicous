def line():
    print("--------------------------------------------------------------")
    
def smooth():
    print("______________________________________________________________")

def surround(string, inp=False):

    if inp:
        line()
        new_string = input(string)
        line()
        return new_string

    line()
    print(string)
    line()

def print_random_title():

    print("\nHello, Welcome to")
    smooth()
    print(" ____   __  ____  ____  __   __    __  ___  __   _  _  ____ ")
    print("/ ___) /  \\(  _ \\(_  _)/ _\\ (  )  (  )/ __)/  \\ / )( \\/ ___)")
    print("\\___ \\(  O ))   /  )( /    \\/ (_/\\ )(( (__(  O )) \\/ (\\___ \\")
    print("(____/ \\__/(__\\_) (__)\\_/\\_/\\____/(__)\\___)\\__/ \\____/(____/")
    smooth()
    print("\n")