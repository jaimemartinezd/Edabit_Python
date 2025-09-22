# Print the Sum of a Current Number and a Previous number
# Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.

curr = 0

for i in range(10):
    print('Current number: ', i, ' Previous number: ', curr, ' Sum = ', i+curr)
    curr = i