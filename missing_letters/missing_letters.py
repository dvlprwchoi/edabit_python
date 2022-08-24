import string


def get_missing_letters(s):
    result = []
    alphabet_list = list(string.ascii_lowercase)
    for x in alphabet_list:
        if x not in s:
            result.append(x)
    return "".join(result)


def get_missing_letters(s):

    letters = 'abcdefghijklmnopqrstuvwxyz'

    return ''.join([i for i in letters if not i in s])


print(get_missing_letters("zyxwvutsrq"))
