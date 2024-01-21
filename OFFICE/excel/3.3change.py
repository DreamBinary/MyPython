from openpyxl import load_workbook
wb=load_workbook(filename='排序与筛选.xlsx')
sheet=wb._sheets[3]
wb.copy_worksheet(sheet)
wb.save(filename='复制.xlsx')




























