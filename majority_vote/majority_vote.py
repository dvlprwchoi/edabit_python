def majority_vote(lst):
    length = len(lst)
    unique_item = list(set(lst))

    for i in unique_item:
        item_count = lst.count(i)
        if(length == 0):
            return None
        elif (item_count > (length/2)):
            return i


print(majority_vote(["A", "A", "A", "B", "C", "A"]))


def majority_vote(lst):
    for i in set(lst):
        if lst.count(i) > len(lst)//2:
            return i
    return None
