import remove_whitespace as rem
file = open('D:\Imperial College London\Year 1\MSE101\Computing\words.txt')


def use_all(File):

    str_char = input('Enter which letters should be used at least one time: ')
    list_char = list(str_char)

    new_file = rem.remove_whitespace(File)
    updated_file = new_file.copy()

    num_lines = len(new_file)
    num = num_lines

    for line in new_file:
        num_show = 0
        for i in list_char:
            if i in line:
                num_show = num_show + 1
        if num_show != len(list_char):
            updated_file.remove(line)
            num = num - 1

    print(updated_file)
    print('The percentage is equal to ', num / num_lines * 100, '%.')
    print('Thanks for using.')

