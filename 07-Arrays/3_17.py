from validators import read_int

numbers = (50, 20, 40, 50, 30, 50)

print('Tuple:', ','.join(str(n) for n in numbers))
value = read_int('Value: ')

count = 0
for number in numbers:
    if number == value:
        count += 1

print('Number of occurrences:', count)
