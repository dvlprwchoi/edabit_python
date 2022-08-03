def word_builder(ltr, pos):
    result = ""
    for i in pos:
        result = result + str(ltr[i])
    return result


def word_builder(ltr, pos):
    return ''.join(ltr[i] for i in pos)


def word_builder(ltr, pos):
    word = []
    for i in pos:
        word.append(ltr[i])
    return ''.join(word)
