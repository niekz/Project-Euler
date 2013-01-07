running = True
counter = 1
current = 2
while running:
    if counter < 10002:
        prime = True
        for x in range(2, current):
            if current%x==0:
                prime = False
        if prime:
            print current
            counter += 1
            current += 1

        else:
            current += 1
    else:
        print current
