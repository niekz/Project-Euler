rows = 41
for rownum in range(rows):
    newValue = 1
    PrintingList = [newValue]
    for iteration in range(rownum):
        newValue = newValue * (rownum-iteration) * 1 / (iteration + 1)
        PrintingList.append(int(newValue))
    print PrintingList
print ()


