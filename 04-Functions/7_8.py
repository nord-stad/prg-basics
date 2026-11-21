from validators import read_int

def f(amount_to_pay):
    coins = 0
    for coin in [5, 2, 1]:
        coins += amount_to_pay // coin
        amount_to_pay = amount_to_pay % coin
    return coins

amount = read_int("Amount to pay:")
print('f(' + str(amount) + ') returns', f(amount))