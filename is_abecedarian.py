import remove_whitespace as rem
file = open('D:\Imperial College London\Year 1\MSE101\Computing\words.txt')


def identity(line):
    """
    This function aims to check whether the word is abecedarian.
    :param line: word
    :return: if it is, return the word.
    """
    key = 0
    list_char = list(line)

    for i in range(len(list_char) - 1):
        if ord(list_char[i + 1]) - ord(list_char[i]) != 1:
            key = 1
            break
    if key == 0:
        return line


def is_abecedarian(file):
    """
    Test function
    :param file: words source
    :return: words list satisfied function identity
    """
    new_file = rem.remove_whitespace(file)
    updated_file = []

    num = 0

    for line in new_file:
        if identity(line) != None:
            num = num + 1
            updated_file.append(line)

    return updated_file

print(is_abecedarian(file))



