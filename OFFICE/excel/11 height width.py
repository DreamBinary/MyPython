from openpyxl import load_workbook
wb=load_workbook(filename='排序与筛选.xlsx')
sheet=wb['成绩表']
sheet.row_dimensions[1].height=50
sheet.column_dimensions['C'].width=50
wb.save('行高列宽.xlsx')

























