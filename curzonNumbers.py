def is_curzon(a):
    potencia = 2 ** a + 1
    mult = 2 * a + 1
    if potencia % mult == 0:
        return True
    else:
        return False

