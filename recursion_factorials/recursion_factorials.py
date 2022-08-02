# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)


def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1
