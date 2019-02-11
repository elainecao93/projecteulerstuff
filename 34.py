# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# upper bound on this is 10,000,000, which is within bring able to brute force

import math

output = 0

for x in range (3, 10000000):
 s = str(x)
 sum = 0
 for ch in s:
  sum += math.factorial(int(ch))
 if sum == x:
  output+=x

print(output)