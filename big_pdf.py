from pathlib import Path
from pypdf import PdfWriter
from directories import *
from pprint import pprint
from itertools import islice

def create_big_pdf(glob_dir, output_path):
    writer = PdfWriter()

    glob_sort = sorted(
        glob_dir.glob("**/*-SVC-*.pdf"),
        key=lambda path: path.name
    )
    glob_dedup = {path.name: path for path in glob_sort}
    glob_dedup.pop("C-SVC-00186 CK Pre-Upgrade Configuration Checklist, 8.x-9.x to 10.x.pdf", None)     # this file destroys everything

    # for filepath in islice(glob_dedup.values(), 100):        # use for testing slices
    for path in glob_dedup.values():
        try:
            writer.append(fr"{str(path)}", import_outline=False)
        except:
            print(f"{path.name} is not a nice file. It was not added to big pdf.")      # just skip a file if it throws an exception
            continue

    for page in writer.pages:
        page.compress_content_streams(level=9)
    writer.compress_identical_objects(remove_identicals=True, remove_orphans=True)  

    with output_path.open(mode="wb") as output_file:
        writer.write(output_file)

if __name__ == "__main__":
    ck_output_path = Path(r"C:\Users\micha\Downloads\ck.pdf")
    idms_output_path = Path(r"C:\Users\micha\Downloads\idms.pdf")
    tomo_output_path = Path(r"C:\Users\micha\Downloads\tomo.pdf")

    create_big_pdf(DIRECTORIES["ck"], ck_output_path)
    create_big_pdf(DIRECTORIES["idms"], idms_output_path)
    create_big_pdf(DIRECTORIES["tomo"], tomo_output_path)