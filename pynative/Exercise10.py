# Merge two lists using the following condition

'''
Given two lists of numbers, write Python code
to create a new list containing odd numbers from the first list and even numbers from the second list.
'''

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

def merge(list1, list2):
    x = []
    for i in list1:
        if i % 2 != 0: x.append(i)
    for w in list2:
        if w % 2 == 0: x.append(w)
    return x

print(merge(list1, list2))