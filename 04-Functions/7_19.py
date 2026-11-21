from validators import read_int

def f(number):
    digits = str(abs(number))
    total = 0
    for char in digits:
        if digits.count(char) > 1:     # this digit appears more than once
            total += int(char)
    return total

number = read_int("Enter number: ", 0, 999999999999999999)
print('f(' + str(number) + ') returns', f(number))