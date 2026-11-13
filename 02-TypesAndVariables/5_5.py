###
# A program that reads the product price and discount (in %)
# from the keyboard, then prints the product price, discount,
# discounted product price, and the difference between
# the product price before and after the discount.
#
from dataclasses import replace


def checking_float(prompt):
    while True:
        text = input(prompt)
        try:
            text = text.replace(',', '.')
            value = float(text)  # try to convert text to float
        except ValueError:
            print("This is not an float, try again.")
            continue  # go back to the beginning of the loop
        if value <= 0:
            print("The side must be greater than 0, try again.")
            continue
        return value  # valid number, exit the function

price = checking_float('Enter price: ')
discount = checking_float('Enter discount %: ')
reduction = price * discount / 100  # how much money we save
price_with_discount = price - reduction
print(f'Price: {price:.2f}')
print(f'Discount: {discount}%')
print(f'Price with discount: {price_with_discount:.2f}')
print(f'Reduction: {reduction:.2f}')