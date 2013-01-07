def gen():
    c = 3
    while True:
        sumoffacts = 0
        for x in str(c):
            sumoffacts += fac(int(x))
        if sumoffacts == c:
            yield c
        c += 1
    
def fac(x):
    s = 1
    for a in range(1, 1+x):
        s *= a
    return s

a = gen()
sums = 0
while True:
    sums += a.next()
    print sums
