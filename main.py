def get_list():
    '''
    l = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    :return:
    '''
    l = [[0, 0, 0, 0, 0, 2, 0, 0, 5],
         [0, 0, 1, 8, 0, 9, 6, 0, 0],
         [0, 2, 0, 1, 0, 0, 0, 7, 0],
         [0, 0, 2, 0, 0, 0, 0, 9, 0],
         [8, 0, 5, 0, 4, 0, 2, 0, 3],
         [0, 4, 0, 0, 0, 0, 5, 0, 0],
         [0, 6, 0, 0, 0, 3, 0, 1, 0],
         [0, 0, 4, 2, 0, 7, 3, 0, 0],
         [9, 0, 0, 4, 0, 0, 0, 0, 0]]

    l = [[0, 0, 3, 0, 1, 8, 0, 0, 0],
         [0, 2, 1, 0, 0, 3, 0, 0, 5],
         [7, 0, 0, 0, 0, 0, 0, 4, 0],
         [8, 0, 0, 0, 0, 1, 0, 0, 0],
         [1, 0, 0, 0, 9, 0, 0, 0, 2],
         [0, 0, 0, 2, 0, 0, 0, 0, 6],
         [0, 8, 0, 0, 0, 0, 0, 0, 3],
         [4, 0, 0, 6, 0, 0, 1, 7, 0],
         [0, 0, 0, 4, 8, 0, 5, 0, 0]]
    return l


def print_list(l):
    for i in range(9):
        for j in range(9):
            print('%-18s' % l[i][j], end='')
        print('\n')


def calculate_possible_digit(l, line, row):
    l_line = [l[line][i] for i in range(9)]
    l_row = [l[i][row] for i in range(9)]
    l_nine_square = [l[line // 3 * 3 + i][row // 3 * 3 + j] for i in range(3) for j in range(3)]

    t_l = [True for i in range(10)]
    t_l[0] = False
    for i in range(9):
        if isinstance(l_line[i], int) and l_line[i] != 0:
            t_l[l_line[i]] = False
        if isinstance(l_row[i], int) and l_row[i] != 0:
            t_l[l_row[i]] = False
        if isinstance(l_nine_square[i], int) and l_nine_square[i] != 0:
            t_l[l_nine_square[i]] = False

    r_l = [i for i in range(1, 10) if t_l[i]]

    if isinstance(l[line][row], list) and not 0 in l_line:
        t_l = list()
        count = 0
        for i in range(9):
            if isinstance(l_line[i], list):
                if l_line[i] == l[line][row]:
                    count += 1
                    if count > 1:
                        t_l.extend(l_line[i])
                    else:
                        continue
                else:
                    t_l.extend(l_line[i])

        for i in range(len(r_l)):
            if r_l[i] not in t_l:
                print(line, row, r_l[i])
                return r_l[i]

    if isinstance(l[line][row], list) and not 0 in l_row:
        t_l = list()
        count = 0
        for i in range(9):
            if isinstance(l_row[i], list):
                if l_row[i] == l[line][row]:
                    count += 1
                    if count > 1:
                        t_l.extend(l_row[i])
                    else:
                        continue
                else:
                    t_l.extend(l_row[i])

        for i in range(len(r_l)):
            if r_l[i] not in t_l:
                print(line, row, r_l[i])
                return r_l[i]

    if isinstance(l[line][row], list) and not 0 in l_nine_square:
        t_l = list()
        count = 0
        for i in range(9):
            if isinstance(l_nine_square[i], list):
                if l_nine_square[i] == l[line][row]:
                    count += 1
                    if count > 1:
                        t_l.extend(l_nine_square[i])
                    else:
                        continue
                else:
                    t_l.extend(l_nine_square[i])

        for i in range(len(r_l)):
            if r_l[i] not in t_l:
                print(line, row, r_l[i])
                return r_l[i]

    if len(r_l) == 1:
        return r_l[0]
    else:
        return r_l


def calculate_possible_list(l, line, row):
    l_line = [l[line][i] for i in range(9)]
    l_row = [l[i][row] for i in range(9)]
    l_nine_square = [l[line // 3 * 3 + i][row // 3 * 3 + j] for i in range(3) for j in range(3)]

    t_l = list()
    for i in range(9):
        if isinstance(l_line[i], list) and l_line[i] != l[line][row]:
            t_l.extend(l_line[i])

    for i in range(len(l[line][row])):
        if l[line][row][i] not in t_l:
            print(line, row, l[line][row][i])
            return l[line][row][i]

    t_l = list()
    for i in range(9):
        if isinstance(l_row[i], list) and l_row[i] != l[line][row]:
            t_l.extend(l_row[i])

    for i in range(len(l[line][row])):
        if l[line][row][i] not in t_l:
            print(line, row, l[line][row][i])
            return l[line][row][i]
    t_l = list()
    for i in range(9):
        if isinstance(l_nine_square[i], list) and l_nine_square[i] != l[line][row]:
            t_l.extend(l_nine_square[i])

    for i in range(len(l[line][row])):
        if l[line][row][i] not in t_l:
            print(line, row, l[line][row][i])
            return l[line][row][i]
    print('aa', t_l)

    return l[line][row]


def calculate_sudoku(l):
    guard = True
    while (guard):
        guard = False
        for line in range(9):
            for row in range(9):
                if (isinstance(l[line][row], int) and l[line][row] == 0) or (isinstance(l[line][row], list)):
                    l[line][row] = calculate_possible_digit(l, line, row)
                    if isinstance(l[line][row], int):
                        print_list(l)
                        print('\n')
                        guard = True
    print_list(l)
    return l


def is_sudoku(l):
    # 判断 行 符合条件
    for line in range(9):
        t_l = [False for i in range(10)]
        for row in range(9):
            t_l[l[line][row]] = True
        isTrue = True
        for i in range(1, 10):
            isTrue = isTrue and t_l[i]
        if not isTrue:
            return False
    # 判断 列 符合条件
    for row in range(9):
        t_l = [False for i in range(10)]
        for line in range(9):
            t_l[l[line][row]] = True
        isTrue = True
        for i in range(1, 10):
            isTrue = isTrue and t_l[i]
        if not isTrue:
            return False

    # 判断 九宫格 符合条件
    for i_line in [0, 3, 6]:
        for j_row in [0, 3, 6]:
            t_l = [False for i in range(10)]
            for line in range(3):
                for row in range(3):
                    t_l[l[i_line + line][j_row + row]] = True
            isTrue = True
            for i in range(1, 10):
                isTrue = isTrue and t_l[i]
            if not isTrue:
                return False

    return True


l = [[6, 4, 3, 5, 1, 8, 2, 9, 7],
     [9, 2, 1, 7, 4, 3, 6, 8, 5],
     [7, 5, 8, 9, 2, 6, 3, 4, 1],
     [8, 7, 2, 3, 6, 1, 9, 5, 4],
     [1, 6, 4, 8, 9, 5, 7, 3, 2],
     [5, 3, 9, 2, 7, 4, 8, 1, 6],
     [2, 8, 7, 1, 5, 9, 4, 6, 3],
     [4, 9, 5, 6, 3, 2, 1, 7, 8],
     [3, 1, 6, 4, 8, 7, 5, 2, 9]]

if __name__ == '__main__':
    # print(is_sudoku(l))
    # print_list(get_list())
    # calculate_possible_digit(get_list(), 8, 0)
    # calculate_sudoku(get_list())
    print(is_sudoku(calculate_sudoku(get_list())))
