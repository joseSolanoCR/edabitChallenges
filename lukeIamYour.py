def relation_to_luke(name):
    relatives = {'Darth Vader':'father', 'Leia':'sister', 'Han':'brother in law','R2D2':'droid'}
    return 'Luke, I am your {}.'.format(relatives.get(name))

print(relation_to_luke('Leia'))