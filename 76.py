target = 100
numbers = range(1,100)
ways = [1]+[0]*target

for x in numbers:
    for i in range(x, target+1):
        ways[i] += ways[i-x]
print ways[target]
