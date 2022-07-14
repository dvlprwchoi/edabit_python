import re


def count_vowels(str):
    return len(re.findall(r'[aeiou]', str))


# def count_vowels(txt):
#     count = 0
#     vowels = 'aeiouAEIOU'
#     for char in txt:
#         if char in vowels:
#             count += 1
#     return count


print(count_vowels("Prediction"))
