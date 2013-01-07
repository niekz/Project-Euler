c = 1
s = 0
inc = 2
end = 1001*1001
while c <= end:
    for x in range(4):
        if c > end:
            break
        s += c
        c += inc
    inc += 2

print c
print s
