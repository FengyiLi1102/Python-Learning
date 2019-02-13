def is_triangle():
    # The input will be the string type, so list.sort() is not well applied here.
    # The input should be converted into int type.
    a = input('What is the length of one stick?\n')
    b = input('What is the length of the second one?\n')
    c = input('What is the length of the last one?\n')
    list_sides = [int(a), int(b), int(c)]
    list_sides.sort()
    if list_sides[0] + list_sides[1] > list_sides[2]:
        print('Yes')
    else:
        print('No')


is_triangle()

