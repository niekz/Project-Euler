def dev(n):
    primes = primes_sieve(n)
    exponents = []
    
    for x in primes:
        ex = 0
        t = True
        while t:
            if n%x==0:
                n /= x
                print n
                ex += 1
            elif ex > 0:
                exponents.append(ex+1)
                t = False
            else:
                t = False
    devs = 1
    for x in exponents:
        devs *= x
    return devs
        
def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes

inc = 2
num = 1
a = True
while a:
    d = dev(num)
    if d > 500:
        print num
        a = False
    num += inc
    inc += 1
