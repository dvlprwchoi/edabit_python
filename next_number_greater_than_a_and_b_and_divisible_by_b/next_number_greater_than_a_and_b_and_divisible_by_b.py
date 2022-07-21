def divisible_by_b(a, b):
    remainder = a % b
    needed = b - remainder
    return a + needed

# floor division


def divisible_by_b(a, b):
    return (a//b + 1)*b


print(divisible_by_b(14, 11))
