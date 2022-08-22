def damage(damage, speed, time):
    time_table = {"second": 1, "minute": 60, "hour": 3600}
    if damage < 0 or speed < 0:
        return "invalid"
    else:
        return damage*speed*time_table[time]


def damage(damage, speed, time):
    secs = {'second': 1, 'minute': 60, 'hour': 3600}
    ans = damage*speed*secs[time]
    return ans if ans > 0 and speed > 0 else 'invalid'
