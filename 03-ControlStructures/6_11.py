from validators import read_float

current_price = read_float("Enter your current price: ")
previous_price = read_float("Enter your previous price: ")

print(f"Current product price: {current_price:.2f}")
print(f"Previous product price: {previous_price:.2f}")

price_reduction = ((previous_price - current_price) / previous_price) * 100

if price_reduction >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {price_reduction}%")