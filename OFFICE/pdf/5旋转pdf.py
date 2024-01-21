import PyPDF2
from PyPDF2 import PdfFileWriter,PdfFileReader
print(dir(PyPDF2))

pdf_reader=PdfFileReader(r"D:\Users\16477\PycharmProjects\pythonProject\pdf\哈哈.pdf")
pdf_writer=PdfFileWriter()
for page in range(pdf_reader.getNumPages()):
    if page%2==0:
        rotation_page=pdf_reader.getPage(page).rotateCounterClockwise(90)
    else:
        rotation_page=pdf_reader.getPage(page).rotateClockwise(90)
    pdf_writer.addPage(rotation_page)
    with open('D:\\Users\\16477\\PycharmProjects\\pythonProject\\pdf\\rotation.pdf','wb')as out:
        pdf_writer.write(out)

























