import math
for x in range(1000):
    for y in range(1000):
        c = math.sqrt(x**2 + y**2)
        if (c+x+y == 1000):
            print x, y, c
            print x*y*c
