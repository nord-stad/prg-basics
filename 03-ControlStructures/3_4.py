###
# Checks whether at least one number entered
# from the keyboard is not negative
#

from validators import read_int

x = read_int('Enter first number: ', -9999)
y = read_int('Enter second number: ', -9999)

if not x < 0 or not y < 0:
    print(f'At least one of the numbers {x} and {y} is not negative')
else:
    print('Both numbers are negative')