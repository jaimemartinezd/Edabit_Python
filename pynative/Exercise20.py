# Print Reverse Number Pattern

def reverse(rows):
    for i in range(rows,0,-1):
        for j in range(0, i):
            print(rows+1-i, end=' ')
        print('\n')

reverse(5)
print('\n')
reverse(7)