#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice
# a square.

#9 = 7 + 2×1^2
#15 = 7 + 2×2^2
#21 = 3 + 2×3^2
#25 = 7 + 2×3^2
#27 = 19 + 2×2^2
#33 = 31 + 2×1^2

#It turns out that the conjecture was false.

#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import math

max_num = 10000

#set up sieve and sieve out primes
numbers = ["none"]*(max_num+1)
for num in range(2, max_num+1):
    if numbers[num] == "none":
        numbers[num] = "prime"
        it = num
        while True:
            it += num
            if it >= max_num:
                break
            numbers[it] = "composite"

for num in range(2, max_num+1):
    if numbers[num] == "prime": #if prime, sieve with plus 2*square
        base = 1
        while True:
            ind = num + 2*base**2
            if ind >= max_num:
                break
            if numbers[ind] == "composite":
                numbers[ind] = "meets condition"
            base += 1
    if numbers[num] == "composite" and num%2 == 1:
        print(num)


"""
for x in range(max_num):
    print(x, numbers[x])
"""