from PyPDF2 import PdfFileWriter,PdfFileReader
pdf_reader=PdfFileReader(r"D:\Users\16477\PycharmProjects\pythonProject\pdf\哈哈.pdf")
for page in range(pdf_reader.getNumPages()):
    pdf_writer=PdfFileWriter()
    pdf_writer.addPage((pdf_reader.getPage(page)))
    with open(f"D:\\Users\\16477\\PycharmProjects\\pythonProject\\pdf\\{page}.pdf",'wb') as out:
        pdf_writer.write(out)




























