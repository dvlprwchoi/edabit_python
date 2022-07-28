def multiply(l):
    new_lst = []
    l_length = len(l)
    for i in range(l_length):
        new_lst.append([])
        for _ in range(l_length):
            new_lst[i].append(l[i])
    return new_lst


def multiply(l):
    return [[i]*len(l) for i in l]


print(multiply(["*", "%", "$"]))
