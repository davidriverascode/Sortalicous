import os
import pyuac

from packages import sortalicous
from packages import options
from packages.tools import formatting as f

@pyuac.main_requires_admin
def main():

    f.print_random_title()
    running = True
    while running:
        running = sortalicous.startup(options.options)

if __name__ == '__main__':
    main()
