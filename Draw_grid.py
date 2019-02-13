def draw_grid(ROW, COLUMN, HEIGHT = 4):
    for row in range(ROW):
        for column_ceiling in range(COLUMN):
            print('+', '- - - -', end=' ')
        print('+')
        for height_row in range(HEIGHT):
            for column_width in range(COLUMN):
                print('|', '  ' * 4, end='')
            print('|')
    for column in range(COLUMN):
        print('+', '- - - -', end=' ')
    print('+')

draw_grid(4, 4, 10)