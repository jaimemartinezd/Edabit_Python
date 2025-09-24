# Check Palindrome Number

'''
A palindrome number is a number that remains the same when its digits are reversed. In simpler terms, it reads the same forwards and backward. For example 121, 5005.

Write a code to check if given number is palindrome.
'''

def palindrome(num):
    x = str(num)
    return str(num) == x[::-1]

print(palindrome(121))
print(palindrome(345))
print(palindrome(5005))