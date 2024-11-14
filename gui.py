from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename
from directory_constants import *
from big_pdf import create_big_pdf

def save_pdf(idms_or_tomo):
    output_path = asksaveasfilename(
            defaultextension="pdf",
            filetypes=[("PDF files", "*.pdf"), ("All Files", "*.*")],
    )
    if not output_path :
        return
    if idms_or_tomo == "idms":
        create_big_pdf(IDMS_DIR, Path(output_path))
    elif idms_or_tomo == "tomo":
        create_big_pdf(TOMO_DIR, Path(output_path))

root = Tk()
root.title("Create a big PDF!!!")
root.eval('tk::PlaceWindow . center')
root.minsize(500, 300)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

button_frame = ttk.Frame(root, padding=(10, 10))
button_frame.grid(row=0, column=0)

idms_save_button = ttk.Button(
    button_frame,
    text='Create big PDF for "iDMS and Precision"',
    command=lambda: save_pdf("idms"),
    padding=(10, 10),
)
idms_save_button.grid(row=0, column=0, padx=5, pady=5)

tomo_save_button = ttk.Button(
    button_frame,
    text='Create big PDF for "TomoTherapy"',
    command=lambda: save_pdf("tomo"),
    padding=(10, 10),
)
tomo_save_button.grid(row=1, column=0, padx=5, pady=5)

root.mainloop()