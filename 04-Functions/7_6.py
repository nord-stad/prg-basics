import card_helper

card_number = '5290312400019022'
masked = card_helper.hide(card_number)

print('f("' + card_number + '") returns "' + masked + '"')