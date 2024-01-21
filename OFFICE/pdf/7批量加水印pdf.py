from PyPDF2 import PdfFileWriter,PdfFileReader
from copy import copy
water=PdfFileReader(r'D:\Users\16477\PycharmProjects\pythonProject\pdf\水印1.pdf')
water_page=water.getPage(0)
pdf_reader=PdfFileReader(r'D:\Users\16477\PycharmProjects\pythonProject\pdf\哈哈.pdf')
pdf_writer=PdfFileWriter()
for page in range(pdf_reader.getNumPages()):
    my_page=pdf_reader.getPage(page)
    new_page=copy(water_page)
    new_page.mergePage(my_page)
    pdf_writer.addPage(new_page)
with open('D:\\Users\\16477\\PycharmProjects\\pythonProject\\pdf\\哈哈水印3.pdf','wb')as out:
    pdf_writer.write(out)

























