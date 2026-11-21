import number_helper
from validators import read_int

x = 2
y = 15

number = read_int('A number: ')

if number_helper.in_range(number, x, y):
    answer = 'yes'
else:
    answer = 'no'

print('Number ' + str(number) + ' in the range <' + str(x) + ',' + str(y) + '>: ' + answer)