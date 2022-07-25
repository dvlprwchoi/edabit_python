def card_hide(card):
    last_four = card[-4:]
    hide = ""
    for _ in range(len(card)-4):
        hide += "*"
    return hide + last_four


def card_hide(card):
    return '*' * (len(card)-4) + card[-4:]


print(card_hide("1234123456785678"))
