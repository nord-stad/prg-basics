def f(expression):
    total = 0
    sign = 1                      # +1 for adding, -1 for subtracting
    for char in expression:
        if char == '+':
            sign = 1
        elif char == '-':
            sign = -1
        else:                     # a digit
            total += sign * int(char)
    return total

expression = input('Enter expression: ')
print('f("' + expression + '") returns', f(expression))