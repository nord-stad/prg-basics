from validators import read_int

decimal = read_int("Enter decimal number: ")

binary = ""
number = decimal

while number > 0:
    remainder = number % 2
    binary = str(remainder) + binary
    number = number // 2

if decimal == 0:
    binary = "0"

print(f"{decimal}(10) = {binary}(2)")