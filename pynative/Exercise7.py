# Find the number of occurrences of a substring in a string

# Write a Python code to find how often the substring “Emma” appears in the given string.

str_x = "Emma is good developer. Emma is a writer"

def emma(str1):
    return str1.count('Emma')

print(emma(str_x))