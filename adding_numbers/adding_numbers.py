def add(n1, n2):
    if n1 == None or n1 == "" or n2 == None or n2 == "":
        return "Invalid Operation"

    return str(int(n1) + int(n2))


def add(n1, n2):
    a = [None, ""]
    if n1 in a or n2 in a:
        return "Invalid Operation"
    return str(int(n1) + int(n2))
