def parse_code(txt):
    txt = txt.split("0")
    keys = ["first_name", "last_name", "id"]
    values = []
    for x in txt:
        if(x != ""):
            values.append(x)
    result_dict = dict(zip(keys, values))
    return result_dict


def parse_code(txt):
    n, s, i = [x for x in txt.split('0') if len(x)]
    return {'first_name': n, 'last_name': s, 'id': i}


print(parse_code("John000Doe000123"))
# parse_code("John000Doe000123") ➞ {
# "first_name": "John",
# "last_name": "Doe",
# "id": "123"
# # }
