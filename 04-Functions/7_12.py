from validators import read_int

def f(n):
    return '/'.join(['*'] * n)

n = read_int("Enter number of asterisks: ")
print('f(' + str(n) + ') returns "' + f(n) + '"')