def create_2d_arr(x, y):
    array = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(0)
        array.append(row)
    return array


array = create_2d_arr(3, 5)   # 3 rows, 5 columns

for row in array:
    for value in row:
        print(value, end=' ')
    print()
