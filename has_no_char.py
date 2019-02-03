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