import calendar_months
from validators import read_int

print('The name of month 7 is', calendar_months.month(7))

number = read_int('Enter month number: ')
print('The name of month', number, 'is', calendar_months.month(number))