import time
start = time.clock()
n = 9

while True:
    l = [n, n*2, n*3, n*4, n*5, n*6]
    a = True
    for x in l:
        if sorted(str(x)) != sorted(str(n)):
            a = False
    if a:
        print (time.clock()-start)*1000,'ms', n
        break
    n+=9
