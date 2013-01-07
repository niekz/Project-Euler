def isP(x):
    return str(x)[::-1] == str(x)

def toBin(x):
    current = x
    binary = ''
    while True:
        if current > 1:
            if current % 2 == 0:
                binary += '0'
            else:
                binary += '1'
            current /= 2
        else:
            binary += '1'
            return int(binary[::-1])

summerize = 0

for x in range(1, 1000000):
    if isP(x):
        if isP(toBin(x)):
            print toBin(x)
            summerize += x

print summerize
