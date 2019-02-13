def is_sorted(L):
    """
    Check whether the list L is in ascending or descending.
    :param L: provided list
    :return: True for ascending and False for descending
    """

    original_list = L.copy()
    check = 0

    L.sort()
    if L == original_list:
        check += 1
        return True

    L.sort(reverse=True)
    if L == original_list:
        check += 1
        return False

    if check == 0:
        return None


