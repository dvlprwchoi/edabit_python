relation = {"Darth Vader": "father", "Leia": "sister",
            "Han": "brother in law", "R2D2": "droid"}


# New syntex
def relation_to_luke(name):
    return f"Luke, I am your {relation[name]}."


# Old syntex
def relation_to_luke(name):
    return "Luke, I am your {}.".format(relation[name])


print(relation_to_luke("Han"))
