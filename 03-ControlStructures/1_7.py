###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#

from validators import read_positive_float

basic_salary = 5000
total_salary = 0
bonus = 0
is_bonus = input('Does the employee receive a bonus? (Y/N): ').strip().upper() == 'Y'

if is_bonus:
    bonus = read_positive_float('Enter bonus in %: ') / 100
    total_salary = basic_salary + basic_salary * bonus
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary:.2f} PLN')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary:.2f} PLN')