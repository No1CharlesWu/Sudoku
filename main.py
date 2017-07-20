import copy


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

    l = [[0, 4, 0, 0, 0, 0, 0, 0, 7],
         [7, 0, 0, 3, 0, 0, 0, 4, 0],
         [0, 0, 2, 7, 0, 9, 6, 0, 0],
         [4, 0, 5, 0, 0, 8, 0, 0, 9],
         [0, 0, 7, 0, 0, 0, 8, 0, 0],
         [8, 0, 6, 0, 0, 3, 2, 0, 4],
         [0, 0, 8, 0, 1, 6, 4, 0, 0],
         [5, 0, 0, 0, 0, 0, 0, 9, 0],
         [0, 2, 0, 0, 9, 0, 0, 0, 6]]

    # l = [[0, 7, 0, 0, 9, 0, 5, 8, 0],
    #      [0, 0, 0, 0, 7, 0, 0, 0, 0],
    #      [3, 0, 0, 5, 0, 0, 6, 7, 0],
    #      [0, 3, 0, 8, 0, 7, 2, 0, 0],
    #      [0, 0, 0, 0, 1, 0, 0, 0, 0],
    #      [0, 0, 6, 3, 0, 9, 0, 1, 0],
    #      [0, 9, 7, 0, 0, 8, 0, 0, 4],
    #      [0, 0, 0, 0, 6, 0, 0, 0, 0],
    #      [0, 1, 8, 0, 5, 0, 0, 2, 0]]
    return l


def print_list(l):
    for i in range(9):
        for j in range(9):
            print('%-10s' % l[i][j], end='')
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
                # print(line, row, r_l[i])
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
                # print(line, row, r_l[i])
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
                # print(line, row, r_l[i])
                return r_l[i]

    if len(r_l) == 1:
        return r_l[0]
    else:
        return r_l


def calculate_sudoku(l):
    guard = True
    count = 0
    while (guard):
        count += 1
        # print('运行：', count, '次')
        guard = False
        for line in range(9):
            for row in range(9):
                if (isinstance(l[line][row], int) and l[line][row] == 0) or (isinstance(l[line][row], list)):
                    temp = calculate_possible_digit(l, line, row)
                    if isinstance(temp, list) and len(temp) == 0:
                        print('wrong')
                    if temp != l[line][row]:
                        l[line][row] = temp
                        # print_list(l)
                        # print('\n')
                        guard = True
    # print('结果:')
    # print_list(l)
    return l


def dfs(l):
    my_copy_list = copy.deepcopy(l)
    index = {'min': 100, 'line': 100, 'row': 100}
    for line in range(9):
        for row in range(9):
            if isinstance(my_copy_list[line][row], list) and (len(my_copy_list[line][row]) < index['min']):
                index['min'] = len(my_copy_list[line][row])
                index['line'] = line
                index['row'] = row

    print(index)
    for i in range(index['min']):
        temp_list = copy.deepcopy(l)
        temp_list[index['line']][index['row']] = my_copy_list[index['line']][index['row']][i]
        temp_list = calculate_sudoku(temp_list)

        print_list(temp_list)

        if is_digit(temp_list):
            if is_sudoku(temp_list):
                print('ok')
                print_list(temp_list)
                return temp_list
            else:
                print('not sudoku')
        else:
            if need_dfs(temp_list):
                print('asb')
                temp_list = dfs(temp_list)

                if temp_list is not None:
                    if is_sudoku(temp_list):
                        return temp_list
            else:
                print('not sudoku')
    return None


def need_dfs(l):
    for line in range(9):
        for row in range(9):
            if isinstance(l[line][row], list) and len(l[line][row]) == 0:
                return False
    return True


def is_digit(l):
    for line in range(9):
        for row in range(9):
            if isinstance(l[line][row], list):
                return False
    return True


def cal(l):
    temp_list = calculate_sudoku(l)
    print_list(temp_list)
    if is_digit(temp_list):
        return temp_list
    else:
        if need_dfs(temp_list):
            temp_list = dfs(temp_list)
            return temp_list


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
    # print(is_sudoku(calculate_sudoku(get_list())))
    print_list(cal(get_list()))
