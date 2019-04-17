#The first two consecutive numbers to have two distinct prime factors are:

#14 = 2 × 7
#15 = 3 × 5

#The first three consecutive numbers to have three distinct prime factors are:

#644 = 2² × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.

#Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

max_num = 1000000 

numbers = ["none"]*(max_num+1)
primes = []
for num in range(2, max_num+1):
    if numbers[num] == "none":
        numbers[num] = "prime"
        primes.append(num)
        it = num
        while True:
            it += num
            if it >= max_num:
                break
            numbers[it] = "composite"

print("flag")
lastnum = 0
streak = 0
for num in range(2, max_num+1):
    if numbers[num] == "composite":
        for prime in primes:
            if num % prime == 0:
                composite = int(num/prime)
                if numbers[composite] == "prime":
                    numbers[num] = {composite, prime} #base case
                    break
                numbers[num] = numbers[composite].copy()
                numbers[num].add(prime)
                if len(numbers[num]) >= 4:
                    if num == lastnum + 1:
                        streak += 1
                    else:
                        streak = 0
                    lastnum = num
                    if streak >= 3:
                        print(num)
                break
            quit