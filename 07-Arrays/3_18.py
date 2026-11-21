import MyArrays

numbers = [7, 3, 8, 5, 2]

smallest_largest = MyArrays.min_max(numbers)

print('Numbers:', ','.join(str(n) for n in numbers))
print('Second largest number:', MyArrays.second_largest(numbers))
print('Difference between largest and smallest:', MyArrays.range_difference(numbers))
print('Median:', MyArrays.median(numbers))
print('Smallest and largest number:', str(smallest_largest[0]) + ',' + str(smallest_largest[1]))
print('Numbers as a string:', MyArrays.to_string(numbers))
