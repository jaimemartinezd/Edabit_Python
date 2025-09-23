# Calculate income tax.

# Calculate income tax for the given income by adhering to the rules below.

income1 = 45000
income2 = 15000
income3 = 25000

def calculate_tax(number):
    result = 0

    if number >= 10000:
        number -= 10000
    else: return 0
    
    if number >= 10000:
        number -= 10000
        result += 10000 / 10 + (number * 20) / 100
        return result
    else: return number / 10

print(calculate_tax(income1))
print(calculate_tax(income2))
print(calculate_tax(income3))