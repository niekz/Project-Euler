foo = 100000
running = True
list = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
while running:
    devisable = True
    for x in list:
        if foo%x!=0:
            devisable = False
            break
    if devisable:
        print foo
        running = False
    else:
        print "Failed : " + str(foo)
    foo += 1
