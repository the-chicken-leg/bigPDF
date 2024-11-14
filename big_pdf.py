from pathlib import Path
from pypdf import PdfWriter
from directories import *
from pprint import pprint

def create_big_pdf(glob_dir, output_path):
    writer = PdfWriter()

    glob_sort = sorted(
        glob_dir.glob("**/*-SVC-*.pdf"),
        key=lambda file: file.name
    )
    glob_dedup = {path.name: path for path in glob_sort}

    for pdf_path in glob_sort[:5]:       # remove slice after testing
        try:
            writer.append(fr"{str(pdf_path)}")
        except:
            continue        # just ignore a pdf if it causes an error, maybe there's a better way

    for page in writer.pages:
        page.compress_content_streams(level=9)
    writer.compress_identical_objects(remove_identicals=True, remove_orphans=True)  

    with output_path.open(mode="wb") as output_file:
        writer.write(output_file)

if __name__ == "__main__":
    ck_output_path = Path(r"C:\PyLocal\big_pdf\ck.pdf")
    idms_output_path = Path(r"C:\PyLocal\big_pdf\idms.pdf")
    tomo_output_path = Path(r"C:\PyLocal\big_pdf\tomo.pdf")

    create_big_pdf(DIRECTORIES["ck"], ck_output_path)
    create_big_pdf(DIRECTORIES["idms"], idms_output_path)
    create_big_pdf(DIRECTORIES["tomo"], tomo_output_path)