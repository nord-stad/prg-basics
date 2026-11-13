from validators import read_int, read_float

products = read_int("Number of products purchased: ")
price = read_float("Product price: ")

if products > 2:
    amount_to_pay = 2 * price + (products - 2) * price * 0.75
else:
    amount_to_pay = products * price

print(f"Amount to pay: {amount_to_pay}")