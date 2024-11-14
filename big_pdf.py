from pathlib import Path
from pypdf import PdfWriter
from directories import *

def create_big_pdf(glob_dir, output_path):
    writer = PdfWriter()

    glob_sorted = tuple(
        sorted(
            glob_dir.glob("**/*-SVC-*.pdf"),
            key=lambda file: file.name
        )
    )

    for pdf_path in glob_sorted[:10]:       # remove slice after testing
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
    idms_output_path = Path(r"C:\PyLocal\big_pdf\iDMS.pdf")
    tomo_output_path = Path(r"C:\PyLocal\big_pdf\Tomo.pdf")

    create_big_pdf(directories["idms"], idms_output_path)
    create_big_pdf(directories["tomo"], tomo_output_path)