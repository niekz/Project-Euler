n = 100
z = 1
s = 0

for x in range(1, n+1):
    z *= x

for x in str(z):
    s += int(x)

print s
