from zipfile import ZipFile

zip_ = ZipFile('../resouces/resouces.zip')
print(zip_.namelist())
text = zip_.read('readme1.txt')
print(text)
zip_.close()

with ZipFile('../resouces/resouces.zip') as zip_:
    print(zip_.namelist())
    text = zip_.read('readme.txt')
    print(text)