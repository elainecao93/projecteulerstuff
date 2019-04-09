#The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

def getval(input):
    output = 0
    for ch in input:
        output+=ord(ch)-64
    return output

triangles = []
for x in range(20):
    triangles.append(x*(x+1)/2)

f = open("p042_words.txt")
input = f.read()
input = input.partition("\"")[2] #parsing file
words = []
while True:
    part = input.partition("\",\"")
    if part[2] == "":
        break
    words.append(part[0])
    input = part[2]

words.append(input.partition("\"")[0])

print(words)

output = 0
for word in words:
    val = getval(word)
    for elem in triangles:
        if val == elem:
            print(word, elem)
            output += 1
print(output)