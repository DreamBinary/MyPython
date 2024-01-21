from docx import Document
doc=Document(r"D:\Users\16477\PycharmProjects\pythonProject\word\猪猪.docx")
list=[
    ['1','2','3'],
    ['2','3','4']
]
table=doc.add_table(rows=2,cols=3)
for row in range(2):
    cells=table.rows[row].cells
    for col in range(3):
        cells[col].text=str(list[row][col])
doc.save(r"D:\Users\16477\PycharmProjects\pythonProject\word\添加表格.docx")




























