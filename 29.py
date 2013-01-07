import math
n = set()

for x in range(2, 101):
    for y in range(2, 101):
        n.add(math.pow(x, y))

print len(n)
        
