import PyPDF2
import pdfplumber
from openpyxl import Workbook
#extract_table() 一页一个表格
#extract_tables() 一页多个表格
with pdfplumber.open('表格.pdf') as p:
    page=p.pages[0]
    table=page.extract_table()
    print(table)
    wb=Workbook()
    sheet=wb.active
    for row in table:
        if not "".join([str(i) for i in row])=="": #去除空行
            sheet.append(row)
    wb.save('pdf表格.xlsx')




























