
def bonus(days):
    calculated_bonus = 0
    bonus_obj = {"0 to 32": 0, "33 to 40": 325,
                 "41 to 48": 550, "greater than 48": 600}
    bonus_33_to_40 = 8 * bonus_obj["33 to 40"]
    bonus_41_to_48 = 8 * bonus_obj["41 to 48"]
    if days > 32 and days <= 40:
        calculated_bonus += (days - 32) * bonus_obj["33 to 40"]
    elif days > 40 and days <= 48:
        calculated_bonus = bonus_33_to_40 + (days-40) * bonus_obj["41 to 48"]
    elif days > 48:
        calculated_bonus = bonus_33_to_40 + bonus_41_to_48 + \
            (days-48) * bonus_obj["greater than 48"]
    return calculated_bonus


def bonus(days):
    return 325*max(0, days-32) + 225*max(0, days-40) + 50*max(0, days-48)


def bonus(days):
    total = 0
    for i in range(1, days+1):
        if 32 < i <= 40:
            total += 325
        if 40 < i <= 48:
            total += 550
        if i > 48:
            total += 600
    return total
