from math import sqrt

def c(n):
    sumofdivs = 1
    for x in range(2, n/2):
        if n%x == 0:
            sumofdivs += x
    return sumofdivs

def d(n):
  s = 1
  t = sqrt(n)
  for i in range(2, int(t)+1):
    if n % i == 0: s += i + n / i
  if t == int(t): s -= t
  return s

limit = 20162
s = 0
abn = set()

for n in range(1, limit):
    if d(n) > n:
        abn.add(n)
    if not any( (n-a in abn) for a in abn ):
        s += n
print s
