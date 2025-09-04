import os

from packages import sortalicous
from packages import options
from packages.tools import formatting as f

if __name__ == '__main__':

    f.print_random_title()
    running = True
    while running:
        running = sortalicous.startup(options.options)
