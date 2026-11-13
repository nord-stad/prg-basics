from validators import read_int

n = read_int("Enter the number of prime numbers: ")

count = 0
number = 2

print("Prime numbers:", end=" ")

while count < n:
    is_prime = True
    divisor = 2
    while divisor < number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        print(number, end=" ")
        count += 1
    number += 1