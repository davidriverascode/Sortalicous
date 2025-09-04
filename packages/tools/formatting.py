import random

def line():
    print("------------------------------------------------------------------------")
    
def smooth():
    print("________________________________________________________________________")

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

    rand_num = random.randint(1, 10)

    if rand_num > 5:

        # print("\nHello, Welcome to")
        # smooth()
        print("       ____   __  ____  ____  __   __    __  ___  __   _  _  ____ ")
        print("      / ___) /  \\(  _ \\(_  _)/ _\\ (  )  (  )/ __)/  \\ / )( \\/ ___)")
        print("      \\___ \\(  O ))   /  )( /    \\/ (_/\\ )(( (__(  O )) \\/ (\\___ \\")
        print("      (____/ \\__/(__\\_) (__)\\_/\\_/\\____/(__)\\___)\\__/ \\____/(____/")
        # smooth()
        # print("\n")

    else:
        # print("Hello, Welcome to")
        # smooth()
        print("  _________              __         .__  .")
        print(" /   _____/ ____________/  |______  |  | |__| ____  ____  __ __  ______")
        print(" \\_____  \\ /  _ \\_  __ \\   __\\__  \\ |  | |  |/ ___\\/  _ \\|  |  \\/  ___/")
        print(" /        (  <_> )  | \\/|  |  / __ \\|  |_|  \\  \\__(  <_> )  |  /\\___ \\ ")
        print("/_______  /\\____/|__|   |__| (____  /____/__|\\___  >____/|____//____  >")
        print("        \\/                        \\/             \\/                 \\/ \n")
        # smooth()
        # print("\n")