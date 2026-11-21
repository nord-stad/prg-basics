def f(dice):
    if dice == '':
        return 0

    best_value = dice[0]
    best_length = 1
    current_length = 1

    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            current_length += 1
        else:
            current_length = 1
        if current_length > best_length:
            best_length = current_length
            best_value = dice[i]
    return int(best_value)

dice = input('Enter dice rolls: ')
print('f("' + dice + '") returns', f(dice))