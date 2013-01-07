import math

def d(n):
    sumofdivs = 1
    for x in range(2, n):
        if n%x == 0:
            sumofdivs += x
    return sumofdivs

bigsum = 0

for x in range(1, 10001):
    b = d(x)
    if x != b and d(b) == x:
        bigsum += x

print bigsum
