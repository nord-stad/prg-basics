def f(detector):
    people = 0
    for sign in detector:
        if sign == '+':
            people += 1
        elif sign == '-':
            people -= 1
        if people >= 3:
            return True    # no need to check the rest
    return False


detector = input('Enter detector record (+/-): ')
print('f("' + detector + '") returns', f(detector))