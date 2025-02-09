'''
Write a function that takes a positive integer num and calculates how many dots exist in a pentagonal shape around the center dot on the Nth iteration.

In the image below you can see the first iteration is only a single dot. On the second, there are 6 dots.
On the third, there are 16 dots, and on the fourth there are 31 dots.
'''

def pentagonal(num):
    if num != 1: return (num-1) * 5 + pentagonal(num-1)
    else: return 1

print(pentagonal(3))