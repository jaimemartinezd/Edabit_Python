# Generate Fibonacci series up to 15 terms

'''
Have you ever wondered about the Fibonacci Sequence? It's a series of numbers in which the next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.

For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13 + 21 = 34.
'''

anterior1 = 0
anterior2 = 1
print(anterior1, anterior2, end=' ')
for i in range(13):
    print(anterior1 + anterior2, end=' ')
    x = anterior1
    anterior1 = anterior2
    anterior2 = anterior2 + x