import remove_whitespace as rw
import in_bisect as ib


def reverse_pair():
    """
    Find all the reversed words in the dictionary provided and print them.
    :return: None
    """

    myfile = open('D:\Imperial College London\Year 1\MSE101\Computing\words.txt')
    word_list = rw.remove_whitespace(myfile)

    for word in word_list:
        original_word = word
        listword = list(word)
        listword.reverse()
        reverse_word = ''.join(listword)
        if ib.is_bisect(word_list, reverse_word) is True:
            print('{} and {}'.format(original_word, reverse_word))

    return None
