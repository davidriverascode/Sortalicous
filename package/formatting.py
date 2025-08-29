def line():
    print("-----------------------------------")
    
def surround(string, inp=False):

    if inp:
        line()
        new_string = input(string)
        line()
        return new_string

    line()
    print(string)
    line()