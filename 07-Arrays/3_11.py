def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


arrays = [
    [64, 34, 25, 12, 22, 11, 90],
    [5, -3, 0, 18, -7, 2],
    [100, 1, 50, 25, 75],
]

for array in arrays:
    print('Before:', array)
    print('After: ', bubblesort(array))
    print()
