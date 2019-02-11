# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# Let f(x) be the sum of the fifth powers of the digits of x, then f(x) < x for all x > 999999 (trivial upper bound)
# brute forcing from 2 to 999999 is inelegant, but isn't too bad and I don't see a cleaner solution

output = 0
for x in range (2, 1000000):
 s = str(x)
 y = 0
 for ch in s:
  y += int(ch)**5
 if x==y:
  print (x)
  output += x
print(output)