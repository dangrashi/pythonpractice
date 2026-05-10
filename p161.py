#Calculate the factorial of a given number using recursion.

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
print(factorial(5))