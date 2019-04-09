#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

#What is the largest n-digit pandigital prime that exists?

import math

def isPrime(input):
    for x in range(2, int(math.sqrt(input))):
        if input%x == 0:
            return False
    return True

# input = list of ints from 1 to 9
# retval = list of ints that are made up of input ints
def getpans(input):
    if len(input) == 1: #base case
        return [input[0]]
    output = []
    for ch in input:
        newlist = input.copy()
        newlist.remove(ch)
        recurse = getpans(newlist) #recurse
        for elem in recurse: #build ints
            output.append(int(str(ch)+str(elem)))
    return output

pans = getpans([1, 2, 3, 4, 5, 6, 7]) #8 and 9 digits are divisible by 9

maxpan = 0

for pan in pans:
    if isPrime(pan) and pan > maxpan:
        maxpan = pan

print(maxpan)