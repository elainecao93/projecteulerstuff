#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

#{20,48,52}, {24,45,51}, {30,40,50}

#For which value of p ≤ 1000, is the number of solutions maximised?

def isSolution(a, p):
    for x in range(a, p):
        #print(a, x, p-a-x)
        if a**2 + x**2 == (p-a-x)**2 and a != 0 and x != 0 and p-a-x != 0:
            print(a, x, p-a-x, p)
            return True
        
    return False

def numSolutions(p):
    output = 0
    for x in range(p):
        if isSolution(x, p):
            output += 1
    return output

answer = 0
max = 0
for x in range(2, 1001):
    num = numSolutions(x)
    if num > max:
        max = num
        answer = x
print(max)
print(answer)