def cout(word, target):
    num = 0
    for i in word:
        if i == target:
            num = num + 1
    return num


print(cout('banana', 'a'))
