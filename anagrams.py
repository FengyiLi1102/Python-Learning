from remove_whitespace import remove_whitespace
fin = open('D:\Imperial College London\Year 1\MSE101\Computing\words.txt')


def anagram(file):
    """
    Print words made with same letters.
    :param file: word list
    :return: a dictionary with tuple('a', 'b', ...): ['xxxx', 'xx', ...] as pairs
    """

    dict1 = dict()

    # Build a normal list
    word_list = remove_whitespace(file)

    for word in word_list:
        # Descend letters in word in a tuple
        w = list(word)
        w.sort()
        w = tuple(w)

        # Dictionary to contain words with same letters
        if w not in dict1:
            dict1[w] = [word]
        else:
            dict1[w].append(word)

    # Sort letter combination with most possibilities
    key_list = []
    for i in dict1:
        key_list.append((len(dict1[i]), dict1[i]))
    key_list.sort(reverse=True)

    for i in key_list:
        if len(i[1]) >= 2:
            print(i[1])

    return dict1


def bingo_word(dimension):
    """
    Find the best word for Bingo game.
    :param dimension: Number of tiles
    :return: None
    """

    len_list = []
    dict1 = anagram(fin)

    # Sort letter combination with most possibilities.
    for i in dict1:
        if len(i) == dimension:
            len_list.append((len(dict1[i]), dict1[i]))
    len_list.sort(reverse=True)

    for i in len_list:
        print(i[1])
