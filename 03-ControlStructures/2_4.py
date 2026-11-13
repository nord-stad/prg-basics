###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.
#

from validators import read_int

number1 = read_int('Enter first number: ')
number2 = read_int('Enter second number: ')

while True:
    operator = input('Enter operator (+, -, *, /): ').strip()
    if operator in ('+', '-', '*', '/'):
        break
    print('Incorrect operator, try again.')

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif number2 == 0:
    print('Error: cannot divide by zero.')
    exit()
else:
    result = number1 / number2

print(f'{number1} {operator} {number2} = {result}')