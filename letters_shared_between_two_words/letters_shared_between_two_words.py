def shared_letters(txt1, txt2):
    count = 0
    for i in set(txt1):
        if i in set(txt2):
            count += 1
    return count


def shared_letters(str1, str2):
    return len(set(str1) & set(str2))


def shared_letters(str1, str2):
    return len([x for x in set(str1) if x in set(str2)])
