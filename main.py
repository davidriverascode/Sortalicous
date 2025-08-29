import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from .package import sortalicous
from .package import options

if __name__ == '__main__':

    running = True
    while running:
        running = sortalicous.startup(options.options)

