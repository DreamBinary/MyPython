from openpyxl import load_workbook
wb=load_workbook(filename='排序与筛选.xlsx')
sheet=wb.get_sheet_by_name('成绩表')
print(sheet)
sheet.delete_cols(idx=2)
sheet.delete_rows(idx=1)
wb.save(filename='删除.xlsx')

#移动格子 正整数下右 负整数左上
sheet.move_range("A1:G1",rows=14,cols=2)
wb.save(filename='移动.xlsx')
























