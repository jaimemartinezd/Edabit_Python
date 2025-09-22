# Print characters present at an even index number
''' Write a Python code to accept a string from the user and display characters present at an even index number.

For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’. '''

word = input('Enter word: ')
print('Original String is: ')
print('Printing only even index chars...')

x = len(word)
for i in range(0, x, 2):
    print(word[i])