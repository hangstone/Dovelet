import math

def sumOfSqures(first, last):
    result = 0
    for i in range(first, last):
        result = result + math.pow(i, 2)
    return result

def squareOfSums(first, last):
    result = 0
    for i in range(first, last):
        result = result + i
    return math.pow(result, 2)

a = squareOfSums(1, 101)
b = sumOfSqures(1, 101)

print (a - b)