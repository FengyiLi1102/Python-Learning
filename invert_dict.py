def invert_dict(dict1):

    dict2 = dict()
    for k in dict1:
        v = dict1[k]
        if v not in dict2:
            dict2.setdefault(v, [k])
        else:
            dict2[v].append(k)

    return dict2
