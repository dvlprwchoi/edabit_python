def name_shuffle(txt):
    first, last = txt.split(" ")
    return "{} {}".format(last, first)


def name_shuffle(txt):
    return "{1} {0}".format(*txt.split())


def nameShuffle(str):
    return ' '.join(reversed(str.split(' ')))
