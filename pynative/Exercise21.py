# Check if a user-entered string contains any digits using a for loop

str = input('Pon tu String:')

def digit(str1):
    bool = False
    for char in str1:
        if '0' <= char <= '9': bool = True
    return bool

print(digit(str))