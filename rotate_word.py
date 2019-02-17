def rotate_word(word, num_rotate):
    """
    This function aims to rotate a word or an integer by a amount of num_rotate in the alphabetical sequence.
    :param word: string or integer
    :param num_rotate: integer
    :return: encrypted word
    """
    encrypted_word = ''
    for letter in word:
        encrypted_word = encrypted_word + chr(ord(letter) + num_rotate)

    return encrypted_word

print(rotate_word('melon', 4))
