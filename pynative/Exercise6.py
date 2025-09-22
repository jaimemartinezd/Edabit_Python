# Exercise 6: Display numbers divisible by 5

# Write a Python code to display numbers from a list divisible by 5

def divisible(list):
    print('Given list is: ', list)
    print('Divisible by 5:')
    for i in list:
        if(i % 5 == 0): print(i)

list1 = [10, 20, 33, 46, 55]

divisible(list1) 