from math import pi
def radians_to_degrees(a):
    angle = a *(180/pi)
    #return "%.1f" % angle
    return round(angle,1)

print(radians_to_degrees(1))