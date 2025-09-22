# Calculate the multiplication and sum of two numbers
# Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000.
# Otherwise, return their sum.

def function1(num1, num2):
    x = num1 * num2
    if x <= 1000: return x
    else: return num1 + num2  

print(function1(20, 40))
print(function1(500,3))