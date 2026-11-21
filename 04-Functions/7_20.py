from validators import read_int

def is_prime(number):
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True

def f(n):
    count = 0
    number = 1
    while count < n:
        number += 1
        if is_prime(number):
            count += 1
    return number

n = read_int("Enter n: ")
print('f(' + str(n) + ') returns', f(n))