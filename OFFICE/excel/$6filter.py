from openpyxl import load_workbook

wb=load_workbook(filename='排序与筛选.xlsx')
sheet=wb._sheets[3]
print(sheet)
#筛选器
sheet.auto_filter.ref=sheet["B1"]
wb.save(filename='筛选器')

























