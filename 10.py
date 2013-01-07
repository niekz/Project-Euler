n = 2000000
foo = 2
sum = 0
while foo < n:
    prime = True
    bar = 2
    while bar < foo:
        if foo%bar==0:
            prime = False
        bar += 1
    if prime:
        sum += foo
        print sum
    foo += 1
print sum
