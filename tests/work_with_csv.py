import csv

with open('../resouces/book.csv') as csvfile:
    table = csv.reader(csvfile)
    for row in table:
        print(row)

with open('../resouces/book.csv') as csvfile:
    row_count = sum(1 for row in csvfile)
    print(row_count)

with open('../resouces/book.csv') as csvfile:
    table = csv.reader(csvfile)
    for line_no, line in enumerate(table,1):
        if line_no == 2:
            print(line)
            print(line[0])
            print(line[1])
            print(line[2])
            print(line[3])