# import math


# def factorial(num):
#     return math.factorial(num)


def factorial(num):
    if num < 1:
        return
    return num * factorial(num-1)
