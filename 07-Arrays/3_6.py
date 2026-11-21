numbers = [15, 8, 31, 47, 2, 19]

total = 0
i = 0
print('Array:', end=' ')
while i < len(numbers):
    print(numbers[i], end=' ')
    total += numbers[i]
    i += 1
print()

print('Arithmetic mean:', round(total / len(numbers), 2))
