###
# Credit card payment
#

from validators import read_float

account_balance = 500
total_payment = read_float('Enter total payment: ')

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')