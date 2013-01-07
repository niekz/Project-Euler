number = 0
for x in range(100, 1000):
    for y in range(100,1000):
        foo = str(x*y)
        if foo[::-1]==foo:
            if int(foo) > number:
                number = int(foo)
print number
