import math

#def t(n):
#    return int(n*(n+1)/2)

def isP(n):
    x = (math.sqrt(24*n + 1) + 1)/6
    if x == int(x):
        return True
    else:
        return False
def genH(n):
    return int(n*(2*n-1))

a = 144
while True:
    if isP(genH(a)):
        break
    a += 1
print genH(a)
