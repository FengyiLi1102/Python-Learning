def inverse_dict(d):
    """
    Inverse the key to the value in a given dictionary.
    :param d:
    :return: the new dictionary with original keys as values and values as keys
    """

    dict1 = dict()
    for keys in d:
        value = d[keys]
        if value not in dict1:
            dict1[value] = [keys]
        else:
            dict1[value].append(keys)

    return dict1
