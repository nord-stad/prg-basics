###
# Checking whether the number
# entered from the keyboard is even or odd
#

from validators import read_int

number = read_int('Enter number: ')

if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')