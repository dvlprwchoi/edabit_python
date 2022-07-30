def makes10(a, b):
    return a == 10 or b == 10 or a+b == 10


def makes10(a, b):
    return 10 in [a, b, a+b]


def makes10(a, b):
    return 10 in (a, b, a+b)
