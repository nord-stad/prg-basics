array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

smallest = array[0][0]
largest = array[0][0]
smallest_pos = (0, 0)
largest_pos = (0, 0)

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] < smallest:
            smallest = array[i][j]
            smallest_pos = (i, j)
        if array[i][j] > largest:
            largest = array[i][j]
            largest_pos = (i, j)

print('Smallest value:', smallest,
      '- row', smallest_pos[0] + 1, 'column', smallest_pos[1] + 1)
print('Largest value:', largest,
      '- row', largest_pos[0] + 1, 'column', largest_pos[1] + 1)
