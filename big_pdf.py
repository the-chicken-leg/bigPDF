from pathlib import Path
from pypdf import PdfWriter
# from itertools import islice      # use for testing slices

from directories import DIRECTORIES

def create_big_pdf(glob_dir, pdf_output_path):
    writer = PdfWriter()

    glob_sort = sorted(
        glob_dir.glob("**/*-SVC-*.pdf"),
        key=lambda filepath: filepath.name
    )
    glob_dedup = {filepath.name: filepath for filepath in glob_sort}
    glob_dedup.pop("C-SVC-00186 CK Pre-Upgrade Configuration Checklist, 8.x-9.x to 10.x.pdf", None)     # this file destroys everything

    added_to_big_pdf = []
    # for filepath in islice(glob_dedup.values(), 10):        # use for testing slices
    for filepath in glob_dedup.values():
        try:
            writer.append(fr"{str(filepath)}", import_outline=False)
            added_to_big_pdf.append(str(filepath.name) + "\n")
        except:
            print(f"{filepath.name} is not a nice file. It was not added to big PDF.")
            continue

    for page in writer.pages:
        page.compress_content_streams(level=9)
    writer.compress_identical_objects(remove_identicals=True, remove_orphans=True)  

    with pdf_output_path.open(mode="wb") as output_file:
        writer.write(output_file)

    contents_output_path = pdf_output_path.parent / f"{pdf_output_path.name}_contents.txt"
    with contents_output_path.open(mode="w", encoding="utf-8") as output_file:
        output_file.writelines(added_to_big_pdf)
    
    return len(added_to_big_pdf)

if __name__ == "__main__":
    ck_output_path = Path(r"C:\Users\micha\Downloads\ck.pdf")
    idms_output_path = Path(r"C:\Users\micha\Downloads\idms.pdf")
    tomo_output_path = Path(r"C:\Users\micha\Downloads\tomo.pdf")

    create_big_pdf(DIRECTORIES["ck"], ck_output_path)
    create_big_pdf(DIRECTORIES["idms"], idms_output_path)
    create_big_pdf(DIRECTORIES["tomo"], tomo_output_path)