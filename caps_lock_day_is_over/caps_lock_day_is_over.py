# def normalize(txt):
#     first = txt[0]
#     rest = txt[1:]
#     if rest.islower():
#         return txt
#     elif rest.isupper():
#         return first + rest.lower()+"!"
#     else:
#         return first + rest


def normalize(txt):
    return txt.capitalize() + ('!' if txt.isupper() else '')


print(normalize("CAPS LOCK DAY IS OVER"))
