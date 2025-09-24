'''
Given the month and year as numbers, return whether that month contains a Friday 13th.
'''

import datetime as dt

def has_friday_13(month, year):
    x = dt.datetime(year, month, 13)
    return x.strftime("%A") == 'Friday'
	
y = has_friday_13(8, 1767)
print(y)