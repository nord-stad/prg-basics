###
# Module with functions operating on an array of numbers
# (written without built-in functions such as max, min, sorted, sum)
#


def _sorted_copy(array):
    """Returns a sorted copy of the array (bubble sort)."""
    result = []
    for value in array:
        result += [value]
    n = len(result)
    for i in range(n):
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def min_max(array):
    """Returns a two-element array: [smallest, largest]."""
    smallest = array[0]
    largest = array[0]
    for value in array:
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value
    return [smallest, largest]


def second_largest(array):
    """Returns the second largest (distinct) element."""
    largest = min_max(array)[1]
    second = None
    for value in array:
        if value != largest and (second is None or value > second):
            second = value
    return second


def range_difference(array):
    """Returns the difference between the largest and smallest value."""
    smallest, largest = min_max(array)
    return largest - smallest


def median(array):
    """Returns the median (the middle value of the ordered numbers)."""
    ordered = _sorted_copy(array)
    n = len(ordered)
    middle = n // 2
    if n % 2 == 1:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def to_string(array):
    """Returns array elements as a string separated by the minus sign."""
    text = ''
    for i in range(len(array)):
        if i > 0:
            text += '-'
        text += str(array[i])
    return text
