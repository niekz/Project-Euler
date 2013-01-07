def d(x):
    if x % 4 == 0:
        if x % 1000 == 0:
            if x % 400 == 0:
                return True
    return False
ass = {1: 6, 2:2, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9: 4, 10: 6, 11: 2, 12: 4}
n = 0

def s(x):
    suns = 0
    reduction = ((x%1000) % 100)
    num = reduction + int( (reduction)/4 )
    for y in range(1, 13):
        if y < 3 and d(y):
            if ((num + ass.get(y) + 1) % 7) == 0:
                suns += 1
        else:
            if ((num + ass.get(y) + 2) % 7) == 0:
                suns += 1
    return suns


for x in range(1901, 2001):
    n += s(x)

print n
