def is_same(i, j, num):
    """
    Check if the numbers are mirror symmetry in the given range
    :param i: starting point
    :param j: ending point
    :param num: given number
    :return: if not, False
    """
    word = str(num).zfill(6)
    while i <= j:
        if word[i] == word[j]:
            pass
        else:
            return False
        i += 1
        j -= 1


def is_palindromic():
    """
    Fine num: initially last four numbers are mirror symmetry
              after +1  last five numbers are mirror symmetry
              after +1  all six numbers are mirror symmetry
    :return: None
    """
    num = 0
    while num <= 999996:
        if is_same(2, 5, num) != False:
            num += 1
            if is_same(1, 5, num) != False:
                num += 1
                if is_same(0,5, num) != False:
                    print(num - 2)
        num = num + 1
