from pathlib import Path
from tkinter.filedialog import asksaveasfilename

from directories import DIRECTORIES
from big_pdf import create_big_pdf

def get_filename_and_save(input_directory):
    output_path = asksaveasfilename(
            defaultextension="pdf",
            filetypes=[("PDF files", "*.pdf"), ("All Files", "*.*")],
    )
    if not output_path :
        return
    print("Creating PDF. This might take a few minutes...")
    create_big_pdf(DIRECTORIES[input_directory], Path(output_path))
    print("PDF created")

input_directory = None
while not input_directory in DIRECTORIES:
    input_directory = input('\nWhich big PDF do want to create? Enter "ck", "idms", or "tomo": ')
print("Select save location...")
get_filename_and_save(input_directory)
input("Press any key to exit")
print("Cleaning up...")