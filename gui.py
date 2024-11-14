from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename
from pathlib import Path
from directories import DIRECTORIES
from big_pdf import create_big_pdf

def save_pdf(input_directory):
    output_path = asksaveasfilename(
            defaultextension="pdf",
            filetypes=[("PDF files", "*.pdf"), ("All Files", "*.*")],
    )
    if not output_path :
        return
    print("Creating PDF. This might take a few minutes...")
    create_big_pdf(DIRECTORIES[input_directory], Path(output_path))
    print("PDF created")

root = Tk()
root.title("Create a big PDF!!!")
root.eval('tk::PlaceWindow . center')
root.minsize(500, 300)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

button_frame = ttk.Frame(root, padding=(10, 10))
button_frame.grid(row=0, column=0)

ck_save_button = ttk.Button(
    button_frame,
    text='Create big PDF for "CyberKnife"',
    command=lambda: save_pdf("ck"),
    padding=(10, 10),
)
ck_save_button.grid(row=0, column=0, padx=5, pady=5)

idms_save_button = ttk.Button(
    button_frame,
    text='Create big PDF for "iDMS and Precision"',
    command=lambda: save_pdf("idms"),
    padding=(10, 10),
)
idms_save_button.grid(row=1, column=0, padx=5, pady=5)

tomo_save_button = ttk.Button(
    button_frame,
    text='Create big PDF for "TomoTherapy"',
    command=lambda: save_pdf("tomo"),
    padding=(10, 10),
)
tomo_save_button.grid(row=2, column=0, padx=5, pady=5)

root.mainloop()