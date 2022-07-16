def calculator(num1, operator, num2):
    if operator == '/' and num2 == 0:
        return "Can't divide by 0!"
    else:
        return eval(str(num1)+operator+str(num2))


def calculator(n1, operator, n2):
    try:
        return eval(str(n1)+operator+str(n2))
    except ZeroDivisionError:
        return "Can't divide by 0!"
