import itertools
def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = set()

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.add(i)

    return sorted(primes)

a = primes_sieve(1000000)
#print len(a)
counter = 0

def rotate (seq):
    for i in range (len (seq)):
        yield int(seq[i:] + seq[:i])

for x in a:
    tempset = set()
    isC = 1
    for y in rotate(str(x)):
        if y not in a:
            isC = 0
            break
    if isC == 1:
        counter += 1

print counter

#for x in a:
 #   if len(str(x)) == 1:
  #      counter += 1
   #     print counter
    #else:
     #   meh = set()
      #  for p in list(itertools.permutations(str(x))):
       #     tempnumber = ''.join(p)
        #    meh.add(int(tempnumber))
        #if meh.issubset(a):
         #   counter += 1
          #  print counter
