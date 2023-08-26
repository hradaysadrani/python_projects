# from pypdf import PdfWriter

# merger = PdfWriter()

# for pdf in ["\Hraday\Python tutorial\Python tutorial projects\PDFMerger\example1.pdf", "\Hraday\Python tutorial\Python tutorial projects\PDFMerger\example2.pdf", "\Hraday\Python tutorial\Python tutorial projects\PDFMerger\example3.pdf"]:
#     merger.append(pdf)

# merger.write("merged-pdf.pdf")
# merger.close()

# The below code will merge pdf in a sequence same as the folder itself.

import os
from PyPDF2 import PdfMerger

x = [a for a in os.listdir() if a.endswith(".pdf")]

merger = PdfMerger()

for pdf in x:
    merger.append(open(pdf, 'rb'))

with open("result.pdf", "wb") as fout:
    merger.write(fout)