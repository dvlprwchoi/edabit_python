import math


def weight(r, h):
    print(math.pi*r**2*h/1000000)
    return round((math.pi * (r/100)**2 * (h/100))*1000, 2)


print(weight(4, 10))
