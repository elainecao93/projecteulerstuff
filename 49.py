#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i)
# each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is
# one other 4-digit increasing sequence.

#What 12-digit number do you form by concatenating the three terms in this sequence?

import math

primes = {}

def isPrime(num):
    for x in range(2, int(math.sqrt(num))+1):
        if num%x == 0:
            return False
    return True

for x in range(1000, 10000):
    if isPrime(x):
        k = "".join(sorted(str(x)))
        if k not in primes:
            primes[k] = []
        primes[k].append(x)

for k in primes:
    if len(primes[k]) < 3:
        continue
    #print(k, primes[k])
    for prime in range(len(primes[k])):
        for otherprime in range(prime+1, len(primes[k])):
            primes[k][prime]
            primes[k][otherprime]
            difference = primes[k][otherprime] - primes[k][prime]
            thirdprime = primes[k][otherprime] + difference
            if (thirdprime) in primes[k]:
                print(primes[k][prime], primes[k][otherprime], thirdprime)