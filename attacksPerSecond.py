def damage(a,b,c):
    if a >= 0 and b >= 0:
        units = {'SECOND': 1, 'MINUTE':60,'HOUR':3600}
        attacks = a * b*units[str.upper(c)]
        return attacks
    else:
        return 'invalid'

print(damage(-23,20,'second'))
# units = {'SECOND': 1, 'MINUTE':60,'HOUR':3600}
