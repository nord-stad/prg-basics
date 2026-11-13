###
# People up to and including 26 years of age are exempt
# from paying taxes in Poland. Write a program that,
# based on the person's age entered from the keyboard,
# prints True if the person is exempt from paying taxes
# and prints False otherwise.
#

def read_age(prompt: str) -> int:
    age = 0
    while True:
        text = input(prompt).strip()  # remove spaces at the beginning and end
        try:
            age = int(text)  # try to convert text to an integer
        except ValueError:
            print("This is not an integer, try again.")
            continue  # go back to the beginning of the loop
        break
    return age


age = read_age('Enter age: ')
no_tax = age < 27  # "up to and including 26" means 26 still counts
print(f'Exemption from paying taxes: {no_tax}')