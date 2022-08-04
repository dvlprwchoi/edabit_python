def reverse_words(words):
    words = words.strip().split(" ")
    words.reverse()
    return " ".join(words)


def reverse_words(words):
    return " ".join(i for i in words.split()[::-1])


print(reverse_words(" hello world! "))
