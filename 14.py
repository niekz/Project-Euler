high = 0
count = 1
n = 13
num = 1

for x in range(1, 1000001):
    n = x
    t = True
    count = 1
    while t:
        if n != 1:
            if n%2==0:
                n /= 2
                count += 1
            else:
                n = 3*n+1
                count += 1
        else:
            t = False 
	    break
    if count > high:
        high = count
        num = x
print num
