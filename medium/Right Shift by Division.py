'''
Write a function that mimics (without the use of >>) the right shift operator and returns the result from the two given integers.
'''

def shift_to_right(x, y):
    return x // (2**y)

print(shift_to_right(80, 3))
print(shift_to_right(-24, 2))
print(shift_to_right(-5, 1))
print(shift_to_right(4666, 6))
print(shift_to_right(3777, 6)) 
print(shift_to_right(-512, 10))