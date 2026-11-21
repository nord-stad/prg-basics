from validators import read_int

def f(x, y):
    total = 0
    for number in range(x, y + 1):
        if number % 2 == 0 and number % 3 == 0 and number % 4 != 0:
            total += number
    return total

x = read_int("Enter x: ")
y = read_int("Enter y: ")
print('f(' + str(x) + ',' + str(y) + ') returns', f(x, y))