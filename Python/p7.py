__author__ = 'Paolo'

import math

number = 100

squareOfSums = 0

sumOfSquares = 0

for i in range(1, number + 1):
    sumOfSquares = sumOfSquares + math.pow(i, 2)
    squareOfSums = squareOfSums + i

squareOfSums = math.pow(squareOfSums, 2)

print sumOfSquares - squareOfSums