import remove_whitespace as rw
myfile = open('D:\Imperial College London\Year 1\MSE101\Computing\words.txt')
words_list = rw.remove_whitespace(myfile)

def is_bisect(word_list, word):
    """
    Find whether the word is in the dictionary or not by using bisect method.
    :param word_list: dictionary provided
    :param word: target worc
    :return: True for in and False for not
    """

    i = len(word_list) // 2

    if len(word_list) == 0:
        return False
    if word_list[i] == word:
        return True
    elif word < word_list[i]:
        return is_bisect(word_list[:i], word)
    else:
        return is_bisect(word_list[i + 1:], word)

