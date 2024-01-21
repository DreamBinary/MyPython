from openpyxl import load_workbook
wb=load_workbook('排序与筛选.xlsx')
sheet=wb['成绩表']
sheet.freeze_panes="C3"
wb.save(filename='冻结.xlsx')



























