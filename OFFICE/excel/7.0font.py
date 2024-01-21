from openpyxl.styles import Font
from openpyxl import load_workbook
wb=load_workbook(filename='排序与筛选.xlsx')
sheet=wb['成绩表']
print(sheet)
#修改字体样式
cell0=sheet['A1:G15']
fo=Font(name='阿里巴巴普惠体',size=20,bold=True,italic=1,color='FF0000')
for i in cell0:
    for j in i:
        j.font=fo
wb.save(filename='字体0.xlsx')




























