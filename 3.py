n = 600851475143
foo = 2
while foo < n:
    prime = True
    bar = 2
    if n%foo==0:
        while bar < foo:
            if foo%bar==0:
                prime = False
            bar += 1
        if prime:
            print foo
    foo += 1
