def find_it(items, name):
    if name in items.keys():
        return "{} is gone...".format(name.title())
    else:
        return "{} is here!".format(name.title())
