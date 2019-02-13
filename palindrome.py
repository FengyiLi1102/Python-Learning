def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1: -1]


def is_palindrome(word):
    """
    Check whether the word is mirror symmetry.
    :param word:
    :return: None
    """
    word_test = list(word)
    word_compare = word_test.copy()
    word_test.reverse()
    if word_compare == word_test:
        print('It is a palindrome word.')
    else:
        print('It is not a palindrome word.')


is_palindrome('reivider')