# def series_resistance(lst):
#     sum_lst = sum(lst)

#     if sum_lst <= 0:
#         return f"{sum_lst} ohm"
#     else:
#         return f"{sum_lst} ohms"

def series_resistance(lst):
    sum_lst = sum(lst)

    if sum_lst <= 1:
        return str(sum_lst) + " ohm"
    else:
        return str(sum_lst) + " ohms"


def series_resistance(lst):
    return "{} {}".format(sum(lst), "ohms" if sum(lst) > 1 else "ohm")


print(series_resistance([0, 0.1]))
print(series_resistance([1.2, 0.3, 0.4]))
print(series_resistance([0, 0]))
