from validators import read_int

def occurs(number, array):
    for value in array:
        if value == number:
            return True
    return False


array = [15, 38, 7, 23, 14]

number = read_int('Number: ')
print('Array:', ' '.join(str(value) for value in array))
if occurs(number, array):
    print('Result: number', number, 'appears in the array')
else:
    print('Result: number', number, 'does not appear in the array')
