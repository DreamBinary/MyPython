from docx import Document
from docx.shared import Cm #设定图片大小
doc=Document(r"D:\Users\16477\PycharmProjects\pythonProject\word\猪猪.docx")
doc.add_picture(r"D:\Users\16477\PycharmProjects\pythonProject\word\pen.png",width=Cm(5),height=Cm(10))
doc.save(r"D:\Users\16477\PycharmProjects\pythonProject\word\添加图片.docx")




























