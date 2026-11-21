def f(palindrome):
    return palindrome == palindrome[::-1]

expression = input('Enter expression: ')
print('f("' + expression + '") returns', f(expression))