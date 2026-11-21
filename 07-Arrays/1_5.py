arr = [1, 2, 3, 4, 5]

def print_array(array):
    print('Array:', str(array).replace(' ', ''))

print_array(arr)

arr[0] = arr[0] - 1
print_array(arr)

arr[len(arr) - 1] = arr[len(arr) - 1] + 4
print_array(arr)

arr[len(arr) // 2] = arr[len(arr) // 2] * 2
print_array(arr)