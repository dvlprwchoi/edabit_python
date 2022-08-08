def show_the_love(lst):
    smallest_num = min(lst)
    smallest_num_index = lst.index(smallest_num)
    addition = 0
    new_lst = []
    for i in lst:
        if i != smallest_num:
            new_lst.append(i * 0.75)
            addition += i * 0.25
        else:
            new_lst.append(i)
    new_lst[smallest_num_index] += addition
    return new_lst


def show_the_love(lst):
    new = [i * 0.75 for i in lst]
    new[lst.index(min(lst))] += sum(lst) - sum(new)
    return new


print(show_the_love([4, 1, 4]))
