from math import log
def solve_for_exp(a, b):
    return round(log(b,a))

print(solve_for_exp(2,1024))