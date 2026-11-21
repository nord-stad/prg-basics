numbers = [15, 8, 31, 47, 2, 19]

print('existed array:', end=' ')
for number in numbers:
    print(number, end=' ')
print()

print('reverse array:', end=' ')
i = len(numbers) - 1          # start from the last index
while i >= 0:
    print(numbers[i], end=' ')
    i -= 1                    # move one position back
print()