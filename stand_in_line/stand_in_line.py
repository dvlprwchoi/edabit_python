# def next_in_line(lst, num):
#     if len(lst) == 0:
#         return "No list has been selected"
#     else:
#         lst.append(num)
#         return lst[1:]


def next_in_line(lst, num):
    return lst[1:] + [num] if lst else "No list has been selected"


print(next_in_line([5, 6, 7, 8, 9], 1))
