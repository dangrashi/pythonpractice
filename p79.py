# 1. Create a set (note: no colons like dictionaries)
fruits = {"apple", "banana", "cherry"}

# 2. Adding items
fruits.add("orange")  # Adds a single item

# 3. Removing items
fruits.remove("banana")  # Removes item; errors if not found
fruits.discard("apple")  # Removes item; does NOT error if missing

# 4. Duplicates are automatically removed
numbers = {1, 2, 2, 3}
print(numbers)  # Output: {1, 2, 3