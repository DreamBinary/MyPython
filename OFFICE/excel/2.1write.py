
from openpyxl import load_workbook
from openpyxl.utils import FORMULAE
#公式
print(FORMULAE)

wb=load_workbook(filename='排序与筛选.xlsx')
sheet=wb.worksheets[3]
print(sheet)
sheet['H1']='平均身高'
for i in range(2,15):
    sheet['H{}'.format(i)]='=AVERAGE(B{}:G{})'.format(i,i)
wb.save(filename='公式.xlsx')





















