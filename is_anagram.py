def is_anagram(str1, str2):
    """
    Check whether two words are made from same characters.
    :param str1: one word
    :param str2: another word
    :return: True for YES and False for NO
    """

    list1 = list(str1)
    list2 = list(str2)

    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False

