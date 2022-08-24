def filter_list(l):
    result = []
    for x in l:
        if type(x) != str:
            result.append(x)
    return result


def filter_list(l):
    return [i for i in l if type(i) == int]


def filter_list(l):
    return [x for x in l if isinstance(x, int)]
