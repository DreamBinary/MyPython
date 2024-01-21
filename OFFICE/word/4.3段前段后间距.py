from docx import Document
from docx.shared import Pt
doc=Document(r"D:\Users\16477\PycharmProjects\pythonProject\word\猪猪.docx")
for paragraph in doc.paragraphs:
    paragraph.paragraph_format.space_before=Pt(12)
    paragraph.paragraph_format.space_after= Pt(12)
doc.save(r"D:\Users\16477\PycharmProjects\pythonProject\word\段前后.docx")




























