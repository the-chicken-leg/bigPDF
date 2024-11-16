from pathlib import Path
from tkinter.filedialog import asksaveasfilename

from directories import DIRECTORIES
from big_pdf_writer import create_writer, compress_writer, write_writer, get_num_files

def main():
    input_directory = None
    while not input_directory in DIRECTORIES:
        input_directory = input('Which big PDF do want to create? Enter "ck", "idms", or "tomo": ')
    get_filename_and_save(input_directory)
    input("Press Enter key to exit")
    print("Cleaning up...") 

def get_filename_and_save(input_directory):
    print("Select save location...")
    output_path = asksaveasfilename(
            defaultextension="pdf",
            filetypes=[("PDF files", "*.pdf"), ("All Files", "*.*")],
    )
    if not output_path :
        return
    print("\nCreating big PDF. This might take a few minutes...")
    writer, added_to_big_pdf = create_writer(DIRECTORIES[input_directory])
    write_writer(compress_writer(writer), added_to_big_pdf, Path(output_path))
    num_files = get_num_files(added_to_big_pdf)
    print(f"\nBig PDF created. {num_files} work instructions included.")

main()