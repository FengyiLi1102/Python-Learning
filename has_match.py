def match(str1, str2):
    """
    Check if two arguments are the same.
    :param str1: arg1
    :param str2: arg2
    :return: Same for True and Different for False
    """

    for letter1, letter2 in zip(str1, str2):
        if letter1 != letter2:
            return False
    return True

