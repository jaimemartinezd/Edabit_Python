# Check Palindrome Number

'''
Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward.
For example, 545 is a palindrome number.
'''

def palindrome(number):
    print('original number ', number)
    str_num = str(number)
    reversed = str_num[::-1]
    if str_num == reversed: print('Yes. Given number is palindrome number')
    else: print('No. given number is not palindrome number')

palindrome(121)
palindrome(123)