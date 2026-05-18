#Find the maximum value in a list without using the built-in max() function

def find_max(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(find_max([10, 50, 30, 90, 20]))