from directories import DIRECTORIES
from gui import get_filename_and_save

input_directory = None
while not input_directory in DIRECTORIES:
    input_directory = input('\nWhich big PDF do want to create? Enter "ck", "idms", or "tomo": ')

print("Select save location...")
get_filename_and_save(input_directory)