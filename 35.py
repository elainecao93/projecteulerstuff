#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#How many circular primes are there below one million?

#sieve this?

isprime = [1]*1000000

isprime[0] = 0
isprime[1] = 0

primes = []

for x in range(0, 1000000):
 if isprime[x] == 1:
  primes.append(x)
  y = 2*x
  while y < 1000000:
   isprime[y] = 0
   y+=x
