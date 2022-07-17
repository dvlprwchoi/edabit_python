def sum_odd_and_even(lst):
    odd = []
    even = []
    for i in lst:
        if (i % 2 == 0):
            even.append(i)
        else:
            odd.append(i)
    return [sum(even), sum(odd)]


def sum_odd_and_even(lst):
    return [sum(i for i in lst if not i % 2), sum(i for i in lst if i % 2)]
