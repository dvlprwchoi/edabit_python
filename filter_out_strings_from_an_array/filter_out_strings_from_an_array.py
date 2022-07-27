def filter_list(lst):
    int_lst = []
    for i in lst:
        if(type(i) == int):
            int_lst.append(i)
    return int_lst


def filter_list(lst):
    return [x for x in lst if type(x) is int]
