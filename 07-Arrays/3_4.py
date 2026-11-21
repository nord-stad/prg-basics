numbers = [-15, 8, -31, 47, -2, 19]

maximum = numbers[0]
minimum = numbers[0]
for number in numbers:
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number

print('Array:', numbers)
print('Maximum:', maximum)
print('Minimum:', minimum)
