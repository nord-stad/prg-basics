arr = [7, 9, 2, 4, 5, 6]
print('arr =', str(arr).replace(' ', ''))

even = []
odd = []
for number in arr:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

arr = even + odd
print('arr =', str(arr).replace(' ', ''))
