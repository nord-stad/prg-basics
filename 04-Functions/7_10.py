from validators import read_int

def f(x, y):
    count = 0
    for number in range(x, y + 1):
        if number < 0 and number % 2 == 0:
            count += 1
    return count

x = read_int("Enter x:", -9999)
y = read_int("Enter y:")

print('f(' + str(x) + ',' + str(y) + ') returns', f(x, y))