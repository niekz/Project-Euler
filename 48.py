number = 1

def last(x):
    counter = x
    newNum = x
    while counter > 1:
        #print newNum
        newNum *= x
        newNum = int(str(newNum)[-10:])
        counter -= 1
    return newNum

for x in range(2, 1000):
    number += last(x)

#print last(3)

print str(number)[-10:]
