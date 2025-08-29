import os
import shutil

def line():
    print("-----------------------------------")
    
def surround(string, input=False):

    if input:
        line()
        new_string = input(string)
        line()
        return new_string

    line()
    print(string)
    line()






#ANCHOR - Outline
# Sort images
# Sort documents based off of content?
# Run on startup
# Allow user to create custom sorts
# Sort games?
# Sort Downloads folder -> installers