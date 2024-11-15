from tkinter.filedialog import asksaveasfilename
from big_pdf import create_big_pdf
from directories import DIRECTORIES
from pathlib import Path

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

if __name__ == "__main__":
    get_filename_and_save(DIRECTORIES["ck"])
    get_filename_and_save(DIRECTORIES["idms"])
    get_filename_and_save(DIRECTORIES["tomo"])