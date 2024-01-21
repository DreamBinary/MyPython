from docx import Document
from docx.shared import Pt,RGBColor
from docx.oxml.ns import qn
doc=Document(r"D:\Users\16477\PycharmProjects\pythonProject\word\猪猪.docx")
for paragraph in doc.paragraphs:
    for run in paragraph.runs:
        run.font.bold=True
        run.font.italic=True
        run.font.underline=True
        run.font.strike=True
        run.font.shadow=True
        run.font.size=Pt(18)
        run.font.color.rgb=RGBColor(225,225,0)
        run.font.name="宋体"
        # 设置中文字体须加以下两行代码
        r=run._element.rPr.rFonts  #?
        r.set(qn("w:eastAsia"),"宋体")  #?

doc.save(r"D:\Users\16477\PycharmProjects\pythonProject\word\字体样式.docx")




























