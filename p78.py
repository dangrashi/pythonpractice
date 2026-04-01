# Creating a set
numbers = {1, 2, 3, 4, 5}

# Adding an element
numbers.add(6)

# Removing an element
numbers.remove(3)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))        # {1,2,3,4,5}
print(a.intersection(b)) # {3}
print(a.difference(b))   # {1,2}

# Display set
print(numbers)