# def stutter(word):
#     stut = word[0:2]
#     sep = '...'
#     ns = F"{stut} {sep} {stut} {sep} {word} "
#     return ns

def stutter(word):
    stut = (word[0:2])
    print(stut)
    sep = '...'
    q='?'
    ns = "%s%s %s %s %s%s" %(stut, sep, stut, sep, word, q)
    return ns

print(stutter('increasing'))