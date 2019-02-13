file = open('D:\Imperial College London\Year 1\MSE101\Computing\words.txt')

def remove_whitespace(File):
    """
    This function aims to remove the whitespace or newlines in each line of the given file
    :param File: given file (txt)
    :return: none
    """

    for line in File:
        new_line = line.strip()
        print(new_line)


def select_word(File, length):
    """
    This function aims to print the line larger than the given length.
    :param File: provided file in txt type
    :param length: expect length + 1 for the line printed
    :return: none
    """
    for line in File:
        new_line = line.strip()
        if len(new_line) > length:
            print(new_line)


def has_no_e(File, char):
    """
    This function aims to print the line without any char and give the percentage of such line in the file
    :param File: provided file
    :return: none
    """
    num = 0
    num_lines = 0
    for line in File:
        new_line = line.strip()
        num_lines = num_lines + 1
        if new_line.find(char) == -1:
            print(new_line)
            num = num + 1
    print('The percentage is equal to ', num / num_lines * 100, ' %.')


remove_whitespace(file)