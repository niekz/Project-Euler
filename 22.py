data = raw_input().split(',')
for x in range(len(data)):
    data[x] = data[x][1:-1]
data.sort()

alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

totalsum = 0

for x in data:
    wordsum = 0
    for y in x:
        wordsum += alph.index(y)+1
    wordsum *= data.index(x)+1
    totalsum += wordsum

print totalsum
