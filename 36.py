#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

#(Please note that the palindromic number, in either base, may not include leading zeros.)

def isStringPal(input):
    for it in range(len(input)):
        if input[it] != input[len(input)-1-it]:
            return False
    return True

def isPal(x):
    return isStringPal(str(x))

def isPal2(x):
    return isStringPal("{0:b}".format(x)) #todo

output = 0
for x in range(0, 1000000):
    if isPal(x) and isPal2(x):
        output += x

print(output)