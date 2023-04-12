def dis(a,b):
    result = a - (a * (b/100))
    return   round(result,2)

print(dis(100,75))