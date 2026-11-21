from validators import read_int

def f(n1, n2, n3):
    return n1 < 0 or n2 < 0 or n3 < 0

n1 = read_int("Enter first number: ", -9999)
n2 = read_int("Enter second number: ", -9999)
n3 = read_int("Enter third number: ", -9999)

print('f(' + str(n1) + ',' + str(n2) + ',' + str(n3) + ') returns', f(n1, n2, n3))