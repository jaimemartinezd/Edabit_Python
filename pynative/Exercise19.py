# Print Alternate Prime Numbers till 20

'''
A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11).
'''

arr = []
for i in range(2,20):
    primo = True
    for j in range(2,i):
        if i % j == 0 and i != j: primo = False
    if primo: arr.append(i)

for i in range(0, len(arr), 2): print(arr[i], end=' ')