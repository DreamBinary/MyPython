from openpyxl.styles import Font
from openpyxl import load_workbook
wb=load_workbook(filename='排序与筛选.xlsx')
sheet=wb.get_sheet_by_name('成绩表')
print(sheet)
cell=sheet['A2']
font=cell.font
print(font.name,font.size,font.bold,font.italic,font.color)
























