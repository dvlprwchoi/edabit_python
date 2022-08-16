def get_indices(lst, el):
    result_lst = []
    for i in range(len(lst)):
        if lst[i] == el:
            result_lst.append(i)
    return result_lst


def get_indices(lst, el):
    return [i for i in range(len(lst)) if lst[i] == el]


print(get_indices([1, 5, 5, 2, 7], 7))
