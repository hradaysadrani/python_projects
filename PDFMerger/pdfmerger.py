from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["\Hraday\Python tutorial\Python tutorial projects\PDFMerger\example1.pdf", "\Hraday\Python tutorial\Python tutorial projects\PDFMerger\example2.pdf", "\Hraday\Python tutorial\Python tutorial projects\PDFMerger\example3.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()