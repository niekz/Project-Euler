marked = [0] * 1000000
value = 3
s = 2
while value < 1000000:
    if marked[value] == 0:
        s += value
        i = value
        while i < 1000000:
            marked = 1
            i += value
    value += 2
print s
