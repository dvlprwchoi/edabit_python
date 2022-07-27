def pluralize(lst):
    new_set = set(lst)
    for i in new_set:
        if (lst.count(i) > 1):
            new_set.remove(i)
            i += "s"
            new_set.add(i)
    return new_set


print(pluralize(["cow", "pig", "cow", "cow"]))
