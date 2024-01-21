from PyPDF2 import PdfFileWriter,PdfFileReader
pdf_reader=PdfFileReader(r'D:\Users\16477\PycharmProjects\pythonProject\pdf\哈哈.pdf')
pdf_writer=PdfFileWriter()
for page in range(pdf_reader.getNumPages()):
    pdf_writer.addPage(pdf_reader.getPage(page))
#加密
pdf_writer.encrypt("123456")
with open('D:\\Users\\16477\\PycharmProjects\\pythonProject\\pdf\\加密.pdf','wb')as out:
    pdf_writer.write(out)


























