def profitable_gamble(prob, prize, pay):
    if (prob * prize) > pay:
        return True
    else:
        return False


def profitable_gamble(prob, prize, pay):
    return prob * prize > pay
