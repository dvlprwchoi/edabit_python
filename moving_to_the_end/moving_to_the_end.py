

# def move_to_end(lst, el):
#     x = lst.count(el)
#     while el in lst:
#         lst.remove(el)
#     lst.extend([el]*x)
#     return lst


def move_to_end(lst, el):
    for item in lst:
        if item == el:
            lst.remove(item)
            lst.append(item)
    return lst


# print(move_to_end([1, 3, 2, 4, 4, 1], 1))
print(move_to_end([7, 7, 7, 6, 6, 6, 6], 7))
