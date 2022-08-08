def lst_ele_sum(args):
    result = []
    sum_list = sum(args)
    for i in args:
        result.append(sum_list-i)
    return result


def lst_ele_sum(nums):
    total = sum(nums)
    return [total - i for i in nums]


print(lst_ele_sum([1, 2, 3, 2, 1]))
