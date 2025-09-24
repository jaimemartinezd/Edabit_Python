# Get an int value of base raises to the power of exponent

'''
Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

Note here exp is a non-negative integer, and the base is an integer.
'''

def exponent(base, exp):
    if(exp >= 0): return base ** exp
    else: return 'El exponente no puede ser un número negativo.'

print(exponent(5,2))
print(exponent(2,5))
print(exponent(3,-1))