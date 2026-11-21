from validators import read_int
from keyboard import input_boolean

def f(number, even):
    total = 0
    for char in str(abs(number)):
        digit = int(char)
        is_even_digit = digit % 2 == 0
        if is_even_digit == even:
            total += digit
    return total

number = read_int('Enter a number: ')
even = input_boolean('Is even? (y/n) ')

print('f(' + str(number) + ',' + str(even) + ') returns', f(number, even))