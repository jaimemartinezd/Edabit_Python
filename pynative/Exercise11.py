# Get each digit from a number in the reverse order.

# For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

number_example = 7536

def reverse(number):
    x = str(number)
    y = x[::-1]
    for i in range(len(y)):
        print(y[i], end=" ")

reverse(number_example)