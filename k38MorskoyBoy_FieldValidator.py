class


ROW_NUM = 10
COL_NUM = 10


def check_diagonal(row_i, col_i, field):
    if row_i !=9 and col_i != 9:
        if field[row_i+1][col_i+1] != 0:
            return True
    if col_i > 0 and row_i !=9:
        if field[row_i+1][col_i-1] != 0:
            return True
    return False



def find_direction(row_i, col_i, field):
    """
    :param row_i:
    :param col_i:
    :param field:
    :return:
    0: no 1s -> submarine
    1 to the right -> 1
    OR
    1 to the bottom -> 2
    if right + bottom -> 3
    """
    counter = 0
    #test horizontal
    if col_i != 9:
        if field[row_i][col_i + 1] == 1:
            counter += 1
    if row_i !=9:
        if field[row_i+1][col_i] == 1:
            counter += 2
        # if field[row_i+1][col_i] != 0:
        #     counter = 3
    return counter


def validate_battlefield(field):
    # write your magic here
    # test if we are getting correct set as 'field'

    # check field for the following:
    # overall ship(1s) count: 20
    # create a dict with following ships: 1:4, 2:3, 3:2, 4:1
    # after that lets find 1s with _for_ cycle: when found update it to '-1'
    # and perform next checks:
    # for every found 1s test its diagonals are 0s, calling a separate function

    # first - horizontal
    # if any adjacent list positions have 1s - count them and -1 from dict,
    # update it to '-1'
    # check if next field lines have 0s on same indexes

    # second vertical: if no adjacent are 1s:
    # check if next field lines have 1s on the same index
    # count them and -1 from dict for the found ship
    # update them to '-1'
    # check if adjacent positions have 0s
    # it's a solo one(submarine): correct it to '-1', -1 from dict

    # continue with for cycle where element == '1'

    # ensure that we are not testing indexes out of bounds
    # check if we can't go negative with dict values
    # test if we are not reaching timeout

    if len(field) != ROW_NUM:
        return False
    ones = 0

    for row in field:
        if len(row) != COL_NUM:
            return False
        ones += row.count(1)
    # print(ones)

    default_ships = {1:4, 2:3, 3:2, 4:1}

    for row_i in range(ROW_NUM):
        # print(row_i, field[row_i])
        for col_i in range(len(field[row_i])):
            # print(col_i, field[row_i][col_i])
            x = field[row_i][col_i]
            if x == 1:
                if check_diagonal(row_i, col_i, field):
                    return False    #look for any diagonal ships
                field[row_i][col_i] = -1
                direction = find_direction(row_i, col_i, field)
                if direction >= 3:
                    return False
                if direction == 0:
                    if default_ships[1] > 0:
                        default_ships[1] -= 1
                    else:
                        return False

                if direction == 1:
                    ship_len = 1
                    for col_j in range(col_i+1,COL_NUM):
                        if check_diagonal(row_i, col_j, field):
                            return False  # look for any diagonal ships
                        field[row_i][col_j] = -1
                        ship_len += 1
                        if ship_len > 4:
                            return False
                        direction = find_direction(row_i, col_j, field)
                        if direction == 0:
                            if default_ships[ship_len] > 0:
                                default_ships[ship_len] -= 1
                                break
                            else:
                                return False
                        if direction in (2, 3):
                            return False
                if direction == 2:
                    ship_len = 1
                    for row_j in range(row_i+1,ROW_NUM):
                        if check_diagonal(row_j, col_i, field):
                            return False  # look for any diagonal ships
                        field[row_j][col_i] = -1
                        ship_len += 1
                        if ship_len > 4:
                            return False
                        direction = find_direction(row_j, col_i, field)
                        if direction == 0:
                            if default_ships[ship_len] > 0:
                                default_ships[ship_len] -= 1
                                break
                            else:
                                return False
                        if direction in (1, 3):
                            return False
    # print(field)


    return sum(default_ships.values()) == 0

print(validate_battlefield([
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]))


