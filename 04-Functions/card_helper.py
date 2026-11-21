def hide(card_number):
    hidden_count = len(card_number) - 6   # digits to replace with '*'
    return card_number[:2] + '*' * hidden_count + card_number[-4:]