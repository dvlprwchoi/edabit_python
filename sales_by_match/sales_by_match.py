def sock_merchant(lst):
    unique_value = list(set(lst))
    pair_num = 0
    for x in unique_value:
        pair_num += (lst.count(x))//2
    return pair_num


def sock_merchant(lst):
    return sum(lst.count(i) // 2 for i in set(lst))


print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))
