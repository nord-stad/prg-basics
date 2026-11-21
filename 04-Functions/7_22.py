def f(name):
    result = ''
    for word in name.split():
        result += word[0]
    return result

name = input('Enter text: ')
print('f("' + name + '") returns "' + f(name) + '"')