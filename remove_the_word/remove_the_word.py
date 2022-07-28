def remove_letters(letters, word):
    for i in word:
        if(i in letters):
            letters.remove(i)

    return letters


print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))
