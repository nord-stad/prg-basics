from validators import read_int

amount = read_int("Enter the amount in PLN: ")

original_amount = amount
coins_5 = amount // 5
amount = amount % 5
coins_2 = amount // 2
amount = amount % 2
coins_1 = amount

print("The amount of PLN", original_amount, "in coins:")
print("5 PLN coins:", coins_5)
print("2 PLN coins:", coins_2)
print("1 PLN coins:", coins_1)