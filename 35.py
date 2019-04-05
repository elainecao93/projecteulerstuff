#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#How many circular primes are there below one million?

import math

#sieve

primes = []
primes.append(2) #hardcoded edge case because lazy

#returns boolean of whether or not the input is prime
def isPrime(input):
 sqrtx = int(math.sqrt(input))
 for iter in range(2, sqrtx+1):
  if input%iter == 0:
   return False
 return True

for x in range(3, 1000000):
 if isPrime(x):
  primes.append(x)

print(len(primes))



#check for circular

#returns boolean of whether or not the input is prime, using list created earlier.
#problem is that this is O(n) so I didn't end up using this because I'm too lazy to implement a log(n) search and the earlier function is sqrt(n)
def isInPrimes(input):
 for iter in primes:
  if iter == input:
   return True
 return False

circulars = []

print("flag")

for x in primes:
 flag = 1
 xstr = str(x)
 lenstr = len(xstr)
 if lenstr == 1: #hardcoded base case
  circulars.append(x)
  continue
 for y in range(lenstr):
  part1 = xstr[lenstr-1]
  part2 = xstr[0:lenstr-1]
  xstr = part1 + part2
  #if isInPrimes(int(xstr)) == False:
  if isPrime(int(xstr)) == False:
   flag = 0
 if flag == 1:
  circulars.append(x)
  

print(circulars)
print(len(circulars))


















