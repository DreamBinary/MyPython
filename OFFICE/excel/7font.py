from openpyxl.styles import Font
from openpyxl import load_workbook
wb=load_workbook(filename='排序与筛选.xlsx')
sheet=wb['成绩表']
print(sheet)
cell=sheet['A2']
fo=Font(name='阿里巴巴普惠体',size=20,bold=True,italic=1,color='FF0000')
cell.font=fo
wb.save(filename='字体.xlsx')

























