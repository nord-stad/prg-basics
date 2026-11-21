def is_subset(array1, array2):
    for value in array1:
        if value not in array2:
            return False
    return True


pairs = [
    ([2, 5, 8], [1, 2, 3, 5, 8, 13]),
    ([2, 4, 8], [1, 2, 3, 5, 8, 13]),
]

for array1, array2 in pairs:
    print('Array1:', array1)
    print('Array2:', array2)
    if is_subset(array1, array2):
        print('Result: the first array is a subset of the second one')
    else:
        print('Result: the first array is NOT a subset of the second one')
    print()
