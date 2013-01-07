def wordVal(x):
    l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = 0
    for i in x:
        #print i
        n += (l.index(i))+1
    return n

triangles = []
for x in range(1000):
    triangles.append(int( (1.0/2.0) * x * (x + 1) ))

words = raw_input().split(",")
howmany = 0
for x in range(len(words)):
    words[x] = words[x][1:-1]
    if triangles.count(wordVal(words[x])) > 0:
        howmany += 1

print howmany
print wordVal('SKY')
