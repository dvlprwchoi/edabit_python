# def area_of_country(name, area):
#     return f"{name} is {str(round(area/1489400, 2))}% of the total world's landmass"


def area_of_country(name, area):
    return name + " is "+"{:.2%}".format(area/148940000)+" of the total world's landmass"


def area_of_country(name, area):
    return "{} is {:.2%} of the total world's landmass".format(name, area / 148940000)


def area_of_country(name, Ar):
    landmass = 148940000
    return "{0} is {1:.2%} of the total world's landmass".format(name, Ar/landmass)


print(area_of_country("USA", 9372610))
