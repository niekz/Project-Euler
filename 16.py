n = 1000
num = 2**n
x = 0
sum = 0
while x < len(str(num)):
    sum += int(str(num)[x])
    x += 1
print sum
