import PyPDF2
import pdfplumber
with pdfplumber.open('哈哈.pdf') as p:
    page = p.pages[0]
    print(page)
print("sdafas")




























