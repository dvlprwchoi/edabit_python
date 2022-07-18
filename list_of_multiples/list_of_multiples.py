def list_of_multiples(num, length):
    result = []
    for i in range(num, num*length+1, num):
        result.append(i)
    return result


def list_of_multiples(num, length):
    return [i*num for i in range(1, length+1)]


def list_of_multiples(num, length):
    return list(range(num, num*length+1, num))


print(list_of_multiples(7, 5))
