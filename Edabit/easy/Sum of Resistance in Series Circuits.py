'''
Create a function that takes an array of values resistance that are connected in series, 
and calculates the total resistance of the circuit in ohms. 
The ohm is the standard unit of electrical resistance in the International System of Units ( SI ).
'''

def series_resistance(lst):
    result = 0
    for i in lst:
        result += i
    return result

print(series_resistance([16, 3.5, 6]))