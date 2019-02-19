def histgram(word):
    """
    Calculate the frequency for each letter showing up in the word.
    :param word: string
    :return: a dictionary containing letter: fre pairs.
    """

    lett_fre_dict = dict()
    for letter in word:
        if letter not in lett_fre_dict:
            lett_fre_dict[letter] = 1
        else:
            lett_fre_dict[letter] += 1

    return lett_fre_dict
