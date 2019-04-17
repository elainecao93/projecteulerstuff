#import math

def mult(x, y):
    return (x*y)%(10**10)

def pow(x, y):
    output = 1
    for _ in range(y):
        output = mult(output, x)
    return output

total = 0
for x in range(1, 1001):
    total += pow(x, x)
    if total > 10**10:
        total -= 10**10
print(total)