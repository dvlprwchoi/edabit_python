def fifth(*arg):
    if(len(arg) < 5):
        return "Not enough arguments"
    else:
        return type(arg[4])


def fifth(*args):
    try:
        return type(args[4])
    except:
        return "Not enough arguments"
