def uncensor(txt, vowels):
    txt_replaced = txt.replace("*", "{}")
    vowels_list = list(vowels)
    return txt_replaced.format(*vowels_list)


print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
