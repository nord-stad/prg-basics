numbers = [15, 8, 31, 47, 2, 19]

total = 0
print('Array:', end=' ')
for number in numbers:
    print(number, end=' ')
    total += number
print()

print('Arithmetic mean:', round(total / len(numbers), 2))
