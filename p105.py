#Find the factorial of 5 using a loop

num, fact = 5, 1
for i in range(1, num + 1):
    fact *= i
print(fact)