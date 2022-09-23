def count(deck):
    result = 0
    if len(deck) == 0:
        return 0
    for char in deck:
        if char in [2, 3, 4, 5, 6]:
            result += 1
        elif char in [7, 8, 9]:
            result += 0
        elif char in [10, "J", "Q", "K", "A"]:
            result -= 1
    return result


def count(deck):
    return sum([1 if str(i) in '23456' else -1 if str(i) in 'AKQJ10' else 0 for i in deck])


def count(deck):
    cards = {2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0,
             9: 0, 10: -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1}
    return sum(cards[n] for n in deck)
