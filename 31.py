# How many different ways can £2 be made using any number of coins?
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

# I like the math here but I'm sure there's a better way of coding this

# does not return correct answer

def max_200(input):
 output = 1
 while input >= 200:
  output += max_100(input)
  input -= 200
 return output

def max_100(input):
 print("100 called on", input)
 output = 1
 while input >= 100:
  output += max_50(input)
  input -= 100
 print("100 returning", output)
 return output

def max_50(input):
 print("50 called on", input)
 output = 1
 while input >= 50:
  output += max_20(input)
  input -= 50
 print("50 returning", output)
 return output

def max_20(input):
 print("20 called on", input)
 output = 1
 while input >= 20:
  output += max_10(input)
  input -= 20
 print("20 returning", output)
 return output

def max_10(input):
 #print("10 called on", input)
 output = 1
 while input >= 10:
  output += max_5(input)
  input -= 10
 #print("10 returning", output)
 return output

def max_5(input):
 #print("5 called on", input)
 output = 0
 while input >= 0:
  output += max_2(input)
  input -= 5
 #print("5 returning", output)
 return output

def max_2(input):
 #print("2 called", input, 1+int(input/2))
 return 1+int(input/2)

print(max_200(200))