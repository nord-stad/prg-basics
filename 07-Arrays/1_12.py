categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

max_index = 0
i = 1
while i < len(expenses):
    if expenses[i] > expenses[max_index]:
        max_index = i
    i += 1

print('The most expensive category:', categories[max_index])
print('Amount:', expenses[max_index])