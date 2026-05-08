# Write a Python function that takes a list and returns a new list with unique elements only.

def remove_duplicates(items):
    return list(set(items))
my_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(my_list))