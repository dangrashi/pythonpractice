#Find the factorial of a number using a loop

n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"Factorial of {n} is {fact}")