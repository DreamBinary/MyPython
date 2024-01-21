from PyPDF2 import PdfFileWriter,PdfFileReader
pdf_reader=PdfFileReader(r'D:\Users\16477\PycharmProjects\pythonProject\pdf\加密.pdf')
#解密
pdf_reader.decrypt('123456')
pdf_writer=PdfFileWriter()
for page in range(pdf_reader.getNumPages()):
    pdf_writer.addPage(pdf_reader.getPage(page))
with open('D:\\Users\\16477\\PycharmProjects\\pythonProject\\pdf\\解密.pdf','wb') as out:
    pdf_writer.write(out)



























