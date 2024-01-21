from openpyxl.styles import Alignment
from openpyxl import load_workbook
wb=load_workbook(filename='排序与筛选.xlsx')
sheet=wb['成绩表']
print(sheet)
cell=sheet['B2']

'''Alignment (self, horizontal=None, vertical=None,
                 textRotation=0, wrapText=None, shrinkToFit=None, indent=0, relativeIndent=0,
                 justifyLastLine=None, readingOrder=0, text_rotation=None,
                 wrap_text=None, shrink_to_fit=None, mergeCell=None)
'''
#alignment=Alignment(horizontal='center',vertical='center',textRotation=45,wrapText=True) 对齐样式
#alignment=Alignment(horizontal='center',vertical='center',textRotation=45) 对齐样式1
alignment=Alignment(horizontal='center',vertical='center') #对齐样式2
cell.alignment=alignment
wb.save(filename='对齐样式2.xlsx')























