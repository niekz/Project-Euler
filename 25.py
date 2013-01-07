def fib():
    fa = 1
    fb = 1
    fn = fa + fb
    yield fn
    while True:
        fa = fb
        fb = fn
        fn = fa + fb
        yield fn

a = fib()
x = a.next()
count = 3
while len(str(x)) < 1000:
    x = a.next()
    count += 1
print count
