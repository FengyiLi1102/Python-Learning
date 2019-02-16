import remove_whitespace as rw
myfile = open('D:\Imperial College London\Year 1\MSE101\Computing\words.txt')


def dict_word():
    """
    Convert a list into a dictionary without values.
    :return: Formed dictionary
    """

    words_list = rw.remove_whitespace(myfile)
    words_dict = dict()
    words_dict = words_dict.fromkeys(words_list)

    return words_dict
