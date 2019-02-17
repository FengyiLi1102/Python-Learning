import read_pronunciation_dict as rpd
import remove_whitespace as rw
import in_bisect as ib


fin = open('D:\Imperial College London\Year 1\MSE101\Computing\c06d.txt')
fin2 = open('D:\Imperial College London\Year 1\MSE101\Computing\words.txt')


def check(dic, word):
    """
    Check if two derived words have the same pronunciation compared with their stemmed word.
    :param dic: pronunciation dictionary
    :param word: stemmed word (string)
    :return: True if YES, False if NO
    """

    if dic[word] == dic[word[1:]]:
        if dic[word] == dic[word[0] + word[2:]]:
            return True
    else:
        return False


def in_dict(dic, word):
    """
      Check if the word from the words list is in the pronunciation dictionary.
      :param dic: pronunciation dictionary
      :param word: string required to be checked
      :return: True if in, False if not
    """

    key_list = list(dic.keys())
    i = 0
    if ib.is_bisect(key_list, word):
        i += 1
    if ib.is_bisect(key_list, word[1:]):
        i += 1
    if ib.is_bisect(key_list, word[0] + word[2:]):
        i += 1

    if i == 3:
        return True


def homophones():
    """
    Find all homophone words in the dictionary provided and print them.
    :return: None
    """
    word_list = rw.remove_whitespace(fin2)
    word_pro_dict = rpd.read_dictionary(fin)

    for word in word_list:
        if in_dict(word_pro_dict, word) and check(word_pro_dict, word):
            print(word)
