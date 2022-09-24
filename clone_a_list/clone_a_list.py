def clone(lst):
    copy_lst = list(lst)
    lst.append(copy_lst)
    return lst


def clone(lst):
    lst.append(lst[:])
    return lst


def clone(lst):
    lst.append(lst.copy())
    return lst


def clone(lst):
    lst_new = [lst]
    return lst + lst_new


print(clone([1, 1]))
