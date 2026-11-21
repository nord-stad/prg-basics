from validators import read_float

numbers = [3.5, 7.2, 1.8, 9.4, 5.0, 6.6, 2.1]

print('Array:', numbers)
value = read_float('Enter value: ')

count = 0
for number in numbers:
    if number > value:
        count += 1

print('Number of elements greater than', value, ':', count)
