# def secret(txt):
#     txtArr = txt.split(".")
#     return "<{0} class='{1} {2} {3}'></{0}>".format(*txtArr)


def secret(txt):
    tag = txt.split('.')[0]
    hclass = ' '.join(txt.split('.')[1:])
    print(hclass)
    return "<{} class='{}'></{}>".format(tag, hclass, tag)


def secret(text):
    tag, *rest = text.split('.')
    return "<{0} class='{1}'></{0}>".format(tag, ' '.join(rest))


print(secret("p.one.two.three"))
