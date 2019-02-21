from histgram import histgram
from inverse_dict import inverse_dict


def most_frequent(word):
    """
    Print frequency of each letter in the word.
    :param word:
    :return: A dictionary containing (letters) : frequency
    """

    value_list = []

    # Inverse the letter with the frequency.
    dic = inverse_dict(histgram(word))
    key_list = list(dic.keys())
    key_list.sort(reverse=True)
    for i in key_list:
        value_list.append(tuple(dic[i]))

    dict1 = dict(zip(value_list, key_list))

    return dict1

