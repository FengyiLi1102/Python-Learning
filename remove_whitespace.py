def remove_whitespace(File):
    """
    This function aims to remove the whitespace or newlines in each line of the given file
    :param File: given file (txt)
    :return: none
    """

    new_file = []
    for line in File:
        new_line = line.strip()
        new_file.append(new_line)

    return new_file

