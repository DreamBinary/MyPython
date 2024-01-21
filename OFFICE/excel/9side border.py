from openpyxl.styles import Side,Border
from openpyxl import load_workbook
wb=load_workbook(filename='排序与筛选.xlsx')
sheet=wb['成绩表']
cell=sheet['C1']
side1=Side(style='thin',color='FF0000')
side2=Side(style='thick',color='FFFF0000')
border=Border(left=side1,right=side1,top=side2,bottom=None)
cell.border=border
wb.save(filename='边框样式.xlsx')

























