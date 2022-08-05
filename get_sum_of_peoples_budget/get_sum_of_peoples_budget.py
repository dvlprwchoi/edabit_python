# def get_budgets(lst):
#     sum = 0
#     for dic in lst:
#         sum += (dic["budget"])
#     return sum


def get_budgets(lst):
    return sum(dic["budget"] for dic in lst)


print(get_budgets([
    {"name": "John", "age": 21, "budget": 23000},
    {"name": "Steve",  "age": 32, "budget": 40000},
    {"name": "Martin",  "age": 16, "budget": 2700}
]))
