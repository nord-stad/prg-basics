array = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

total = 0
for row in array:
    total += row[len(row) - 1]   # last element of the row

print('Sum of the last column:', total)
