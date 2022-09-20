import math


def count(n):
    if n == 0:
        return 1
    elif n < 0:
        n *= -1
    return math.floor(math.log10(n)+1)
