lol = []
rows = 100 #Number of rows in the file

for x in range(rows):
    lol.append(map(int, raw_input().split()))

depth = len(lol) - 2

while depth >= 0:
    for x in range(depth+1):
        lol[depth][x] += max(lol[depth+1][x], lol[depth+1][x+1])
    depth += -1;

print lol[0][0]
