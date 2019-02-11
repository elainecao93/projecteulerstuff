#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

#trivially this can only be aa x bbb = cccc or a x bbbb = cccc

solutions = []

for x in range (1, 10):
 for y in range (1000, 10000):
  prod = x * y
  if prod > 9999:
   break
  tostr = str(prod) + str(x) + str(y)
  sortedstr = ''.join(sorted(tostr))
  if sortedstr == '123456789':
   solutions.append(prod)

for x in range (10, 100):
 for y in range (100, 1000):
  prod = x * y
  if prod > 9999:
   break
  tostr = str(prod) + str(x) + str(y)
  sortedstr = ''.join(sorted(tostr))
  if sortedstr == '123456789':
   solutions.append(prod)

solutions = sorted(solutions)
output = 0
for i in range (0, len(solutions)):
 if i == 0 or solutions[i] != solutions[i-1]:
  output += solutions[i]

print(output)