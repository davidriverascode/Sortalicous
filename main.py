import os

from packages import sortalicous
from packages import options

if __name__ == '__main__':

    running = True
    while running:
        running = sortalicous.startup(options.options)
