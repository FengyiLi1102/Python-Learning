def cumsum(L):
    """
    Give a new list with ith element equal to the sum of previous numbers.
    :param L: Provided list
    :return: result list
    """
    new_L =[]
    acc_sum = 0
    for index in range(0, len(L)):
        acc_sum += L[index]
        new_L.append(acc_sum)

    return new_L