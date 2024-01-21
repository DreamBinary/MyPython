from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
doc=Document(r"D:\Users\16477\PycharmProjects\pythonProject\word\猪猪.docx")
for paragraph in doc.paragraphs:
    paragraph.paragraph_format.line_spacing=5.0
doc.save(r"D:\Users\16477\PycharmProjects\pythonProject\word\行间距.docx")



























