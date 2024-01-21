from openpyxl import load_workbook
wb=load_workbook(filename='排序与筛选.xlsx')
sheet=wb._sheets[3]
print(sheet)
sheet.title='成绩表（修改）'
print(sheet)
wb.save(filename='改名sheet.xlsx')


























