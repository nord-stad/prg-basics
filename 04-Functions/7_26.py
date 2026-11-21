def f(text):
    return '-'.join(text)

text = input('Enter text: ')
print('f("' + text + '") returns "' + f(text) + '"')