def series_resistance(a):
    res = sum(a)
    if res == 1:
        unit=' ohm'
    else:
        unit = ' ohms'
    return str(res) + unit


print(series_resistance([0.5,0.5]))