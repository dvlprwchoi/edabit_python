def repetition(txt, n):
    return txt * n


def repetition(txt, n):
    return '' if not n else txt + repetition(txt, n-1)
