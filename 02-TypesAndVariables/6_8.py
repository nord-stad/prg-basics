###
# A program that calculates
# how many letters are between two given letters
#

def read_letter(prompt: str) -> str:
    while True:
        letter = input(prompt).strip().upper()  # remove spaces, convert to uppercase
        if len(letter) != 1:
            print("Enter exactly one letter, try again.")
            continue
        if not ('A' <= letter <= 'Z'):
            print("This is not a letter A-Z, try again.")
            continue
        break  # valid letter, exit the loop
    return letter


first = read_letter('Enter first letter: ')
last = read_letter('Enter last letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
number_of_letters = max(abs(last_letter_code - first_letter_code) - 1, 0)
print(f'Between {first} and {last} is ls{number_of_letters} letters')