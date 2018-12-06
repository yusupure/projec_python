tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

for i in range(len(tableData[0])):
    for k in range(len(tableData)):
        print(tableData[k][i].ljust(20),end=' ')
    print('\n')