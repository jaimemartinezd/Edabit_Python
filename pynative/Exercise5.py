# Check if the first and last numbers of a list are the same

# Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.

def medir_len(arrayZ):
    return arrayZ[0] == arrayZ[-1] # array[-1] devuelve el valor del elemento en la última posición del array.

numbers_x = [10, 20, 30, 40, 10]
# output True

numbers_y = [75, 65, 35, 75, 30]
# Output False

print(medir_len(numbers_x))
print(medir_len(numbers_y))