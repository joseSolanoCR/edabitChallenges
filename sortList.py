def asc_des_none(a,b):
    lista = a
    order = b
    if order.upper() == "ASC":
        lista.sort()
        return lista
    if order.upper() == "DES":
        lista.sort(reverse=True)
        return lista
    if order.upper() == "NONE":
        return lista

print(asc_des_none([1,9,7,8],'None'))




# def calculator(a,b,c):
#     try:
#         OPERATORS = {'+': 'add', '-': 'sub', '*': 'mul', '/': 'truediv'}
#         method = '__%s__' % OPERATORS[b]