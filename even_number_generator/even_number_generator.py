def find_even_nums(num):
    result = []

    for i in range(1, num+1):
        if i % 2 == 0:
            result.append(i)
    return result


def find_even_nums(num):
    return [i for i in range(1, num+1) if i % 2 == 0]
