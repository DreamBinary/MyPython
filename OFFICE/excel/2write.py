from openpyxl import load_workbook
wb=load_workbook(filename='排序与筛选.xlsx')
sheet=wb.active
print(sheet)
sheet['E17']='笨蛋'
#wb.close()
wb.save(filename='笨蛋.xlsx')

#插入行
data=[
    ['不要',44.0,32.0,94.0,67.0,60.0,91.0]
     ]
for row in data:
    sheet.append(row)
wb.save(filename='不要.xlsx')

data1=[
    ['不要'],[44.0],[32.0,94.0,67.0,60.0,91.0]
     ]
for row in data1:
    sheet.append(row)
wb.save(filename='不要2.xlsx')

#插列

#插入指定位置行
sheet2=wb._sheets[0]
print(sheet2)
sheet2.insert_rows(3)
wb.save(filename='插行.xlsx')























