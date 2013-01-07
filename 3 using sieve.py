def primes_sieve(limit):
    limitn = limit+1
    #not_prime = set()
    #primes = []
    largest = 1
    i = 2
    #for i in range(2, limitn):
    while i < limitn:
       # if i in not_prime:
          #  continue

        f = i*2
        #for f in range(i*2, limitn, i):
        while f < limitn:
            #not_prime.add(f)
            f += i
        #primes.append(i)
        if i > largest:
            largest = i
        i += 1
        print i
    return largest
print primes_sieve(600851475143)

