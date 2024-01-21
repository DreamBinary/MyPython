from openpyxl import load_workbook
wb=load_workbook(filename='排序与筛选.xlsx')
#删除sheet
sheet2=wb['成绩表']
print(sheet2)
wb.remove(sheet2)
wb.save(filename='删除sheet.xlsx')




























