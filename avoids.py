import remove_whitespace as rem
file = open('D:\Imperial College London\Year 1\MSE101\Computing\words.txt')


def avoids(File):

    num = 0
    new_file = rem.remove_whitespace(File)
    updated_file = new_file.copy()
    num_lines = len(new_file)

    forb_words = input('Enter your first forbidden word: ')
    if forb_words != 'Done!':
        while forb_words != 'Done!':
            for line in new_file:
                if line.find(forb_words) != -1:
                    updated_file.remove(line)
                    num = num + 1
            new_file = updated_file.copy()
            forb_words = input('Enter your forbidden words: ')

        print(new_file)
        print('The percentage is equal to ', num / num_lines * 100, '%.')
        print('Thanks for using.')
    else:
        print('Thanks for using.')


