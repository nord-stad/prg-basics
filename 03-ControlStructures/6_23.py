from validators import read_int

number = read_int("Enter number: ")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")