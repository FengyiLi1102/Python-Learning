import rotate_word as rtw
import remove_whitespace as rmw
fin = open('D:\Imperial College London\Year 1\MSE101\Computing\words.txt')


def rotate_pairs(myfile):

    words_list = rmw.remove_whitespace(myfile)

    words_dict = dict()
    for letter in words_list:
        words_dict[letter] = None

    for letter in words_list:
        for i in range(1, 14):
            if rtw.rotate_word(letter, i) in words_dict:
                words_dict[rtw.rotate_word(letter, i)] = letter
                print('{} {}'.format(rtw.rotate_word(letter, i), letter))

