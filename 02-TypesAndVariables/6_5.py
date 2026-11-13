###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#

def read_phone(prompt):
    while True:
        phone = input(prompt).strip()  # remove spaces at the beginning and end
        try:
            int(phone)  # only a test, the result is not saved
        except ValueError:
            print("Phone number must contain only digits, try again.")
            continue
        if len(phone) != 9:
            print(f"Phone number must have 9 digits, you entered {len(phone)}, try again.")
            continue
        break  # valid number, exit the loop
    return phone

phone = read_phone('Enter phone number: ')

formatted = phone[0:3] + '-' + phone[3:6] + '-' + phone[6:9]  # 3 groups of 3 digits
print(f'Phone number: {formatted}')