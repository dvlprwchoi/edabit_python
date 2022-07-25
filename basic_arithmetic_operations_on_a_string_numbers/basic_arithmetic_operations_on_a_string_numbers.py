# def arithmetic_operation(n):
#     a, op, b = n.split()
#     if op == "//" and b == "0":
#         return -1
#     elif op == "+":
#         return int(a) + int(b)
#     elif op == "-":
#         return int(a) - int(b)
#     elif op == "*":
#         return int(a) * int(b)
#     else:
#         return int(a) / int(b)


def arithmetic_operation(equation):
    '''
    Returns the result of evaluating the string equation
    '''
    from operator import add, sub, floordiv, mul

    OPS = {'+': add, '-': sub, '*': mul, '//': floordiv}
    a, op, b = equation.split()

    try:
        return OPS[op](int(a), int(b))
    except ZeroDivisionError:
        return -1


print(arithmetic_operation("12 + 12"))
