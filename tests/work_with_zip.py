import zipfile

zip_ = zipfile.ZipFile('../resources/resouces.zip')
print(zip_.namelist())
text = zip_.read('readme1.txt')
print(text)
zip_.close()

with zipfile.ZipFile('../resources/resouces.zip') as zip_:
    print(zip_.namelist())
    text = zip_.read('readme.txt')
    print(text)

new_arch = zipfile.ZipFile('../resources/resources1.zip', 'w')
new_arch.write('../resources/items.xls')
new_arch.write('../resources/items2.xlsx')
new_arch.close()

with zipfile.ZipFile('../resources/resources2.zip', 'w') as myzip:
    myzip.write('../resources/items.xls')
    myzip.write('../resources/items2.xlsx')
    myzip.close()

with zipfile.ZipFile('../resources/resouces.zip') as zp:
    print(zp.infolist())

