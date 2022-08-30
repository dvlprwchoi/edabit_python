def simon_says(lst1, lst2):
    new_lst1 = lst1[:len(lst1)-1]
    new_lst2 = lst2[1:]
    if(new_lst1 == new_lst2):
        return True
    else:
        return False


print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))
