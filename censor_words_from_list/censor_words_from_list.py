def censor_string(txt, lst, char):
    txt_lst = txt.split(" ")
    for i in lst:
        replacement = char * len(i)
        for j in txt_lst:
            if(j == i):
                txt_lst[txt_lst.index(j)] = replacement
    return " ".join(txt_lst)


def censor_string(txt, lst, character):
    for word in lst:
        txt = txt.replace(word, character*len(word))
    return txt


print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))
