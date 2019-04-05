#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import math

def isPrime(input):
    sqrtx = int(math.sqrt(input))
    for iter in range(2, sqrtx+1):
        if input%iter == 0:
            return False
    return True

def isTruncatableLeft(input):
    if input == 1:
        return False
    if input == 1 or input == 2 or input == 3 or input == 5 or input == 7: #base case
        return True
    if not isPrime(input):
        return False
    sin = str(input)
    output = sin[1:len(sin)]
    return isTruncatableLeft(int(output))

def isTruncatableRight(input):
    if input == 1:
        return False
    if input == 2 or input == 3 or input == 5 or input == 7: #base case
        return True
    if not isPrime(input):
        return False
    sin = str(input)
    output = sin[0:len(sin)-1]
    return isTruncatableRight(int(output))

output = 0
for x in range(10, 1000000):
    if isTruncatableLeft(x) and isTruncatableRight(x):
        print(x)
        output += x
print(output)