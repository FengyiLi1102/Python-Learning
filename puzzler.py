file = open('D:\Imperial College London\Year 1\MSE101\Computing\words.txt')

def puzzler(word):

    i = 0
    num = ''
    while i < len(word) - 1:
        if ord(word[i]) - ord(word[i + 1]) == 0:
            num = num + '0'
        else:
            num = num + '1'
        i = i + 1

    if num.find('01010') != -1:
        return True
    else:
        return False


for line in file:
    word = line.strip()
    if puzzler(word):
        print(word)
