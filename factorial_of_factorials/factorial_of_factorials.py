import math


def facts(n):
    return math.factorial(n)


def fact_of_fact(n):
    total = 1
    for i in range(n, 1, -1):
        total = total*facts(i)
    return total


# def fact_of_fact(n):
#     result = 1

#     def factorial(n):
#         if n == 0:
#             return 1
#         return n * factorial(n-1)
#     for i in range(1, n+1):
#         result *= (factorial(i))
#     return result


print(fact_of_fact(4))
