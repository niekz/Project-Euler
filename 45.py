def t(n):
    return int(n * (n+1) / 2)

def p(n):
    return int(n * (3 * n - 1 ) /2)

def h(n):
    return int(n * (2 * n - 1 ) )

x = 286

def getP(x):
    z = 165
    while True:
        current = p(z)
        if current == t(x):
            yield z
        if current < t(x):
            current = p(z+1)
            if current > t(x):
                yield 0
        z += 1

def getH(x):
    z = 143
    while True:
        current = h(z)
        if current == t(x):
            yield z
        if current < t(x):
            current = h(z+1)
            if current > t(x):
                yield 0
        z += 1
a = getP(x)
b = getH(x)
while True:
    if getP(x).next() > 0:
        if getH(x).next() > 0:
            print t(x)
            break
    x += 1
