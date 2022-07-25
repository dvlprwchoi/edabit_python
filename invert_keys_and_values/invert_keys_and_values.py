def invert(dct):
    # for k, v in dct.items():
    #     print(k, v)

    inverted = {value: key for key, value in dct.items()}
    return inverted


def invert(dct):
    return {dct[i]: i for i in dct}


print(invert({"z": "q", "w": "f"}))
