# Determine if a string is a palindrome (reads the same forward and backward). 

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

# Test
print(is_palindrome("Radar"))
