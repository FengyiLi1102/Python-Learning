import remove_whitespace as rem
file = open('D:\Imperial College London\Year 1\MSE101\Computing\words.txt')


def use_only(File):
    """
    This function aims to find words that only use provided characters.
    :param File: Words source
    :return: None
    """
    str_char = input('Enter which letters only can be used: ')
    list_char = list(str_char)

    new_file = rem.remove_whitespace(File)
    updated_file = new_file.copy()

    num_lines = len(new_file)
    num = num_lines

    for line in new_file:
        num_show = 0
        for i in list_char:
            num_show = num_show + line.count(i)
        if num_show != len(line):
            updated_file.remove(line)
            num = num - 1

    print(updated_file)
    print('The percentage is equal to ', num / num_lines * 100, '%.')
    print('Thanks for using.')
