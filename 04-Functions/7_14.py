from validators import read_int

def f(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '%':
        return number1 % number2
    elif operator == '**':
        return number1 ** number2
    else:
        return None

number1 = read_int("Enter first number: ")
number2 = read_int("Enter second number: ")
operator = input("Enter operator (+ - * % **): ")

result = f(number1, number2, operator)

if result is None:
    print('Unknown operator:', operator)
else:
    print('f(' + str(number1) + ',' + str(number2) + ', "' + operator + '") returns', result)