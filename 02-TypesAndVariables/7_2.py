###
# A program that checks whether the password length
# read from the keyboard is correct.
#
password = input('Enter password: ')
password_ok = len(password) >= 8  # "at least 8" means 8 is still OK
print(f'Password length is valid: {password_ok}')