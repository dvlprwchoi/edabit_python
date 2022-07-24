def find_odd(lst):
    for x in lst:
        count = lst.count(x)
        if count % 2 != 0:
            return x


print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
