# def concat(lst1, lst2):
#     return lst1+lst2


def concat(lst1, lst2):
    return [*lst1, *lst2]


print(concat([4, 5, 1], [3, 3, 3, 3, 3]))
