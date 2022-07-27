def sum_missing_numbers(lst):
    consecutive_num = []
    missing_num = []
    for i in range(min(lst), max(lst)+1):
        consecutive_num.append(i)
    if (lst == consecutive_num):
        return 0
    else:
        for i in consecutive_num:
            if i not in lst:
                missing_num.append(i)
    return sum(missing_num)


print(sum_missing_numbers([17, 16, 15, 10, 11, 12]))


def sum_missing_numbers(lst):
    return sum(range(min(lst), max(lst) + 1)) - sum(lst)
