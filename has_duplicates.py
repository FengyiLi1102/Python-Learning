def has_duplicates(alist):
    """
    Check whether there is any character showing up for more than one times.
    :param alist: provided list
    :return: True for YES and False for NO
    """
    for char in alist:
        if alist.count(char) != 1:
            return True

    return False

