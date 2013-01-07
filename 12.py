import math
def dev(n, primes):
    exponents = []
    
    for x in primes:
        ex = 0
        t = True
        while t:
            if n%x==0:
                n /= x
                #print n
                ex += 1
            elif ex > 0:
                exponents.append(ex+1)
                t = False
            else:
                t = False
        if n < x:
            break
        elif n > x:
            return -1
    devs = 1
    for x in exponents:
        devs *= x
    return devs
        
def primes_sieve(limit, primes):
    
    #primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)
        print primes
    return primes


not_prime = set()
inc = 2
num = 1
limit = int(2*math.sqrt(num))
limitn = limit+1
prim = primes_sieve(int(2*math.sqrt(num)), [])
a = True
while a:
    d = dev(num, prim)
    if d == -1:
        prim = primes_sieve(int(2*math.sqrt(num)), prim)
        d = dev(num, prim)
        #print d
    #print d
    if d > 500:
        print num
        a = False
    num += inc
    inc += 1
    print d
