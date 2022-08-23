def reverse(arg):
    if type(arg) != bool:
        return "boolean expected"
    else:
        return not arg


def reverse(arg):
    return not arg if type(arg) == bool else 'boolean expected'
