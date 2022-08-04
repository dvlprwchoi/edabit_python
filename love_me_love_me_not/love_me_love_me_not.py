def loves_me(n):
    result = ""
    if n == 1:
        result += "LOVES ME"
    else:
        for i in range(n):
            if(i % 2 == 0):
                result += 'Loves me, '
            else:
                result += 'Loves me not, '
        splitted_result_list = result.split(", ")
        splitted_result_list.pop()
        splitted_result_list[-1] = splitted_result_list[-1].upper()
        result = ", ".join(splitted_result_list)

    return result


def loves_me(n):
    arr = (['Loves me', 'Loves me not']*n)[:n]
    arr[-1] = arr[-1].upper()
    return ', '.join(arr)


print(loves_me(6))
