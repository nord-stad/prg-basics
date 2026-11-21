from validators import read_int

def f(n):
    previous, current = 0, 1
    for i in range(n - 1):
        previous, current = current, previous + current
    return previous

n = read_int("Enter n: ")
print('f(' + str(n) + ') returns', f(n))