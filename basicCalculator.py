def calculator(a,b,c):
    try:
        OPERATORS = {'+': 'add', '-': 'sub', '*': 'mul', '/': 'truediv'}
        method = '__%s__' % OPERATORS[b]
        return getattr(a,method)(c)
    except Exception as e:
        if e: 'division by zero'
        return "Can't divide by 0!"

print(basicCalc(2,'/',0))