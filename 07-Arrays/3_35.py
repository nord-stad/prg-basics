def transpose_matrix(m):
    rows = len(m)
    columns = len(m[0])
    result = []
    for j in range(columns):
        new_row = []
        for i in range(rows):
            new_row.append(m[i][j])
        result.append(new_row)
    return result


def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=' ')
        print()


matrices = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],
    [[5, 6, 7, 8]]
]

for m in matrices:
    print('Matrix:')
    print_matrix(m)
    print('Transposed:')
    print_matrix(transpose_matrix(m))
    print()
