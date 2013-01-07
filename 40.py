lol = ''
for x in xrange(1000000):
    lol += str(x)
n = 1
x = 1
while x < 1000000:
    n *= int(lol[x])
    x *= 10
print n
