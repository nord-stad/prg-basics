###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#

swift = input('Enter SWIFT code: ').strip().upper()  # remove spaces, convert to uppercase
print(f'Bank Code: {swift[0:4]}')  # characters 0-3
print(f'Country Code: {swift[4:6]}')  # characters 4-5