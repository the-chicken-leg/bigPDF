from pathlib import Path
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename

from directories import DIRECTORIES
from big_pdf import create_big_pdf
from gui import get_filename_and_save

input_directory = input('Which big PDF do want to create? Enter "ck", "idms", or "tomo": ')
while not input_directory in DIRECTORIES:
    input_directory = input('Which big PDF do want to create? Enter "ck", "idms", or "tomo": ')

get_filename_and_save(input_directory)