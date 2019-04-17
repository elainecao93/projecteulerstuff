#The prime 41, can be written as the sum of six consecutive primes:

#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.

#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

#Which prime, below one-million, can be written as the sum of the most consecutive primes?

import math

primes = []
maxnum = 1000000

def isPrime(num):
    for x in range(2, int(math.sqrt(num))+1):
        if num%x == 0:
            return False
    return True

for x in range(2, maxnum+1):
    if isPrime(x):
        primes.append(x)

print("blah")

maxlen = 0
maxprime = 0
for x in range(len(primes)):
    thisprime = 0
    flag = 0
    step = x
    while thisprime < maxnum:
        thisprime += primes[step]
        step += 1
        #print("bah")
        if thisprime in primes and step-x > maxlen:
            maxlen = step-x
            maxprime = thisprime
            print(primes[x], maxlen, maxprime)

print(maxlen, maxprime)