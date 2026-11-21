def f(password):
    if len(password) < 6:
        return False
    for char in password:
        if password.count(char) > 1:
            return False
    return True

password = input('Enter password: ')
print('f("' + password + '") returns', f(password))