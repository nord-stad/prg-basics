###
# Calculates the sum of the digits in a number
#
from helpers.validators import read_int

def sum_digits(number):
    number = abs(number)        # ignore the minus sign
    total = 0
    for digit in str(number):   # iterate over each character
        total += int(digit)     # convert back to int and add
    return total


any_number = read_int('Enter integer number: ')
result = sum_digits(any_number)
print('The sum of the digits in the number', any_number, 'is', result)