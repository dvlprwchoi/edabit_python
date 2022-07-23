

# def format_date(date):
#     m, d, y = date.split('/')
#     return ''.join((y, d, m))


# def format_date(date):
#     a, b, c = date.split('/')
#     return c + b + a


def format_date(date):
    arry = date.split('/')
    arry.reverse()
    return ''.join(arry)


print(format_date("01/15/2019"))
