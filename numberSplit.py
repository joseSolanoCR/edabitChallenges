def number_split(n):
    first = n//2
    second = n - first
    return [first,second]


print(number_split(9))