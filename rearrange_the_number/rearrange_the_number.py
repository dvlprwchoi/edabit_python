def rearranged_difference(num):
    min_num = int("".join(sorted(str(num))))
    max_num = int("".join(sorted(str(num), reverse=True)))
    return max_num-min_num


print(rearranged_difference(972882))
