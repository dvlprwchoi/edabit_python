def even_or_odd(lst):
    if len(lst) == 0:
        lst = [0]
    if sum(lst) % 2 == 0:
        return 'even'
    else:
        return 'odd'


def even_or_odd(lst):
    return 'odd' if sum(lst) % 2 else 'even'
