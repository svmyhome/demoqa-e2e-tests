''''''

'''
These is best pattern
'''
with open('../readme1.txt', 'a') as file:
    file.write('2222222\n')

with open('../readme1.txt', 'r+') as file:
    data = file.read()
    print(data)

with open('../readme1.txt', 'r+') as file:
    data = file.readline()
    print(data)

with open('../readme1.txt', 'r+') as file:
    for i in file:
        print(i)
'''
These are anti-patterns. You must to close 
'''
file = open('../readme.txt', 'w')
file.write('cskmcksmdkcm')
file.close()

file = open('../readme1.txt', 'a')
file.write('1111111111\n')
file.close()

file = open('../readme1.txt',)
data = file.read()
print(data)
file.close()


file = open('../readme1.txt',)
data = file.readline()
print(data)
file.close()

