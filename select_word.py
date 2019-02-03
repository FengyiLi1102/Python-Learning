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