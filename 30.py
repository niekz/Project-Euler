import math
s = 0

def gen():
    num = 2
    meh = 0
    while True:
        for x in str(num):
            meh += math.pow(int(x), 5)

        if meh == num:
            yield num

        num += 1
        meh = 0

generator = gen()

for x in range(100):
    s += generator.next()
    print s
