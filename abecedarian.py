file = open('D:\Imperial College London\Year 1\MSE101\Computing\words.txt')

def abecedarian(word):

    for i in range(len(word) - 1):
        if word[i] < word[i+1]:
            return False
    print(word)

