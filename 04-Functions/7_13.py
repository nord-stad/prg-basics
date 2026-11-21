from validators import read_int

def f(n):
    result = ''
    for number in range(1, n + 1):
        result += str(number)
    return result

n = read_int("Enter n: ")
print('f(' + str(n) + ') returns "' + f(n) + '"')