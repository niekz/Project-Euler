sumSquare = 0
squareSum = 0
for x in range(1, 101):
    sumSquare += x**2
    squareSum += x
squareSum = squareSum**2
print sumSquare
print squareSum
print squareSum-sumSquare
