def to_list(dct):
    return [list(item) for item in sorted(dct.items())]


print(to_list({"c": 1, "b": 2}))
