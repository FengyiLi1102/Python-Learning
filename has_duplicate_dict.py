def has_duplicate_dict(l):

    dict1 = dict()
    for e in l:
        if e not in dict1:
            dict1[e] = 1
        else:
            return True

    return False
