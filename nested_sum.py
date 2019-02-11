def nested_sum(L):
    """
    Sum all the numbers in the list including nested lists and digits.
    :param L: provided list
    :return: result of sum
    """

    sum_lists = 0
    for nested_list in L:
        if type(nested_list) == list:
            sum_lists += sum(nested_list)
        elif type(nested_list) == int or float:
            sum_lists += nested_list

    return sum_lists
