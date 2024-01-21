from PyPDF2 import PdfFileWriter,PdfFileReader
pdf_reader=PdfFileReader(r"D:\Users\16477\PycharmProjects\pythonProject\pdf\哈哈.pdf")
pdf_writer=PdfFileWriter()
for page in range(pdf_reader.getNumPages()-1,-1,-1):
    pdf_writer.addPage(pdf_reader.getPage(page))
with open('D:\\Users\\16477\\PycharmProjects\\pythonProject\\pdf\\倒叙排序.pdf','wb')as out:
    pdf_writer.write(out)


























