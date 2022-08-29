def index_of_caps(word):
    result = []
    for (index, char) in list(enumerate(word)):
        if char.isupper():
            result.append(index)
    return result


print(index_of_caps("eQuINoX"))


def index_of_caps(word):
    return [index for index, letter in enumerate(word) if letter.isupper()]
