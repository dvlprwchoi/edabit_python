def profit(info):
    return round((info["sell_price"] - info["cost_price"]) * info["inventory"])


def profit(info):
    [a, b, c] = info.values()
    return round((b-a)*c)


def profit(info):
    cp = info.get('cost_price')
    sp = info.get('sell_price')
    i = info.get('inventory')

    total = (sp-cp)*i

    return round(total)


print(profit({
    "cost_price": 32.67,
    "sell_price": 45.00,
    "inventory": 1200
}))
