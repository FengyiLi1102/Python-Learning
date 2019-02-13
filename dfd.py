def identity(line):

    key = 0
    list_char = list(line)

    for i in range(len(list_char) - 1):
        if ord(list_char[i + 1]) - ord(list_char[i]) != 1:
            key = 1
            break
    if key == 0:
        return line


print(identity('bdfd'))