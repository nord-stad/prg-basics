from validators import read_int

def f(number1, number2, number3):
    largest = max(number1, number2, number3)
    smallest = min(number1, number2, number3)
    return largest - smallest

number1 = read_int("Enter first number: ")
number2 = read_int("Enter second number: ")
number3 = read_int("Enter third number: ")
print('f(' + str(number1) + ',' + str(number2) + ',' + str(number3) + ') returns', f(number1, number2, number3))