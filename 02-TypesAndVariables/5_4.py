###
# A program that reads an amount including VAT (gross) from the keyboard,
# then calculates and prints the VAT value and the amount without VAT (net)
# with two decimal places.
#
vat_rate = 0.23  # 23%
gross = 0

while True:
    text = input('Enter amount including VAT: ')  # text from the keyboard
    text = text.replace(",", ".")  # replace comma with dot
    try:
        gross = float(text)  # amount with vat as a number
    except ValueError:
        print("This is not a number, try again.")
        continue  # go back to the beginning of the loop
    break  # valid number, exit the loop

net = gross / (1 + vat_rate)  # amount without vat
vat = gross - net  # vat value
print(f'Amount with VAT: {gross:.2f}')
print(f'VAT {vat_rate:.0%}: {vat:.2f}')
print(f'Amount without VAT: {net:.2f}')