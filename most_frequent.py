from histgram import histgram
from inverse_dict import inverse_dict


def most_frequent(word):
    """
    Print frequency of each letter in the word.
    :param word:
    :return: None
    """

    dic = inverse_dict(histgram(word))
    key_list = list(dic.keys())
    key_list.sort(reverse=True)
    for key in key_list:
        print('{} {}'.format(key, dic.get(key)))

