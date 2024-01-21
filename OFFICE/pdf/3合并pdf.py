import os

from PyPDF2 import PdfFileMerger,PdfFileReader,PdfFileWriter
pdf_writer=PdfFileWriter()
# for i in range(1,len(os.listdir(r"D:\Users\16477\PycharmProjects\pythonProject\pdf\pdf"))+1):
#     print(i*50+1,(i+1)*50)
pdf_reader1=PdfFileReader('D:\\Users\\16477\\PycharmProjects\\pythonProject\\pdf\\表格.pdf')
pdf_reader2=PdfFileReader('D:\\Users\\16477\\PycharmProjects\\pythonProject\\pdf\\哈哈.pdf')
for page in range(pdf_reader1.getNumPages()):
    pdf_writer.addPage(pdf_reader1.getPage(page))

for page in range(pdf_reader2.getNumPages()):
     pdf_writer.addPage(pdf_reader2.getPage(page))
with open("D:\\Users\\16477\\PycharmProjects\\pythonProject\\pdf\\merge.pdf",'wb') as out:
    pdf_writer.write(out)
























