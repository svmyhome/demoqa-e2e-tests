import xlrd

xls_table = xlrd.open_workbook('../resouces/items.xls')
print(xls_table.nsheets)
print(xls_table.sheet_names())
sheet1 = xls_table.sheet_by_index(0)
sheet2 = xls_table.sheet_by_index(1)
print(sheet1.ncols)
print(sheet1.nrows)
print(sheet2.ncols)
print(sheet2.nrows)
print(sheet1.cell_value(rowx=2, colx= 1))
for rx in range(sheet1.nrows):
    print(sheet1.row(rx))