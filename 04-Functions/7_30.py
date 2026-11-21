from validators import read_int

def sum_natural(n):
    if n <= 1:
        return n

    return n + sum_natural(n - 1)


n = read_int("Enter a natural number n: ")
print('The sum of natural numbers in the range <1,' + str(n) + '> is', sum_natural(n))