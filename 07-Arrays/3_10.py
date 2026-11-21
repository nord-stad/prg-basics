array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]

print('Numbers only in the first array:', end=' ')
for number in array1:
    found = False
    for other in array2:
        if number == other:
            found = True
    if not found:
        print(number, end=' ')
print()
