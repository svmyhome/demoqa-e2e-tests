import zipfile

# with zipfile.ZipFile('../resources/resources2.zip') as zip_:
#     print(zip_.namelist())
#     text = zip_.read('../resources/readme33.txt')
#     # table = zip_.read('../resources/book.csv')
#     zip_.extractall('../resources/archive')
#     # assert '2222222\r\n2222222\r\n' == text
#     # print(text)
#     # print(table)
#     zip_.close()

# zip_ = zipfile.ZipFile('../resources/resouces.zip')
# print(zip_.namelist())
# text = zip_.read('readme1.txt')
# print(text)
# zip_.close()
#
# with zipfile.ZipFile('../resources/resouces.zip') as zip_:
#     print(zip_.namelist())
#     text = zip_.read('readme.txt')
#     print(text)
#
#
# new_arch = zipfile.ZipFile('../resources/resources1.zip', 'w')
# new_arch.write('../resources/items.xls')
# new_arch.write('../resources/items2.xlsx')
# new_arch.close()
#
# with zipfile.ZipFile('../resources/resources2.zip', 'w') as myzip:
#     myzip.write('../resources/items.xls')
#     myzip.write('../resources/items2.xlsx')
#     myzip.write('../resources/book.csv')
#     myzip.write('../resources/ISTQB_CTFL_PT_Syllabus_2018_GA.pdf')
#     myzip.write('../resources/readme33.txt')
#     myzip.close()
# #
# with zipfile.ZipFile('../resources/resouces.zip') as zp:
#     print(zp.infolist())



