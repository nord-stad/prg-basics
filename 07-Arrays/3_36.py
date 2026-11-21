def to_1d(array_2d):
    result = []
    for row in array_2d:
        for value in row:
            result.append(value)
    return result


arrays = [
    [[2, 3], [1, 5]],
    [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]],
    [[2, 1], [3, 5], [7, 4], [2, 6]]
]

for array in arrays:
    print('2D:', array)
    print('1D:', to_1d(array))
    print()
