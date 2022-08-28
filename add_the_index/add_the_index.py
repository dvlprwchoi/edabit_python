# def add_indexes(lst):
#     result = []
#     enum_lst = list(enumerate(lst))
#     for (x, y) in enum_lst:
#         result.append(x+y)
#     return result


def add_indexes(lst):
    return [number+index for index, number in enumerate(lst)]


print(add_indexes([0, 0, 0, 0, 0]))
print(add_indexes([1, 2, 3, 4, 5]))
