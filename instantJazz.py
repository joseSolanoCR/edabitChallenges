def jazzify(a):
    new_a =[]
    for x in a:
        if '7' not in x:
            new_a.append( x+'7')
        else:
            new_a.append( x )
    return new_a

print(jazzify(["A", "B7","G"]))