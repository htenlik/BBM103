import sys


def input_initialization(input_text):
    row_high = [int(x) for x in input_text.readline().split()]
    row_base = [int(x) for x in input_text.readline().split()]
    col_high = [int(x) for x in input_text.readline().split()]
    col_base = [int(x) for x in input_text.readline().split()]  # first 4 row read.

    table = [line.strip().split() for line in input_text]  # rest of is table.

    return row_high, row_base, col_high, col_base, table


def horizontal_checker(table, row_high, row_base):
    for row in range(len(table)):
        b_number = 0
        h_number = 0  # resetting for every row.
        for col in range(len(table[0])):
            if table[row][col] == "B":
                b_number += 1
            if table[row][col] == "H":
                h_number += 1

        if (row_high[row] == -1 or row_high[row] == h_number) and (row_base[row] == -1 or row_base[row] == b_number):
            continue
        else:
            return False
    return True


def vertical_checker(table, col_high, col_base):
    for col in range(len(table[0])):
        b_number = 0  # resetting for every column.
        h_number = 0
        for row in range(len(table)):
            if table[row][col] == "B":
                b_number += 1
            elif table[row][col] == "H":
                h_number += 1
        if (col_high[col] == -1 or col_high[col] == h_number) and (col_base[col] == -1 or col_base[col] == b_number):
            continue
        else:
            return False
    return True


def checker(table, row, col):
    if table[row][col] == "B":  # checking for every neighbor.
        if 0 < row and "B" == table[row-1][col]:
            return False
        elif row < len(table)-1 and "B" == table[row+1][col]:
            return False
        elif 0 < col and "B" == table[row][col-1]:
            return False
        elif col < len(table[0])-1 and "B" == table[row][col+1]:
            return False
        else:
            return True

    elif table[row][col] == "H":  # same for H.
        if 0 < col and "H" == table[row-1][col]:
            return False
        elif row < len(table)-1 and "H" == table[row+1][col]:
            return False
        elif 0 < col and "H" == table[row][col-1]:
            return False
        elif col < len(table[0]) - 1 and "H" == table[row][col+1]:
            return False
        else:
            return True
    else:  # else is not important including N.
        return True


def game_solver(table, row, col, row_high, row_base, col_high, col_base):
    if col == len(table[0]):
        if row == len(table)-1:  # if it's end of the table check constraints.
            if vertical_checker(table, col_high, col_base) and horizontal_checker(table, row_high, row_base):
                return True  # if it's okay for constraints finish code.
            else:
                return False
        col = 0
        row += 1

    if table[row][col] == "L":
        table[row][col] = "H"
        table[row][col + 1] = "B"
        if checker(table, row, col):  # backtracking.
            if game_solver(table, row, col + 1, row_high, row_base, col_high, col_base):
                return True
        table[row][col] = "B"
        table[row][col + 1] = "H"
        if checker(table, row, col):
            if game_solver(table, row, col + 1, row_high, row_base, col_high, col_base):
                return True
        table[row][col] = "N"
        table[row][col + 1] = "N"
        if checker(table, row, col):
            if game_solver(table, row, col + 1, row_high, row_base, col_high, col_base):
                return True
        table[row][col] = "L"  # if it's couldn't find a solution, reset table.
        table[row][col+1] = "R"

    elif table[row][col] == "U":
        table[row][col] = "H"  # backtracking.
        table[row+1][col] = "B"
        if checker(table, row, col):
            if game_solver(table, row, col + 1, row_high, row_base, col_high, col_base):
                return True
        table[row][col] = "B"
        table[row+1][col] = "H"
        if checker(table, row, col):
            if game_solver(table, row, col + 1, row_high, row_base, col_high, col_base):
                return True
        table[row][col] = "N"
        table[row+1][col] = "N"
        if checker(table, row, col):
            if game_solver(table, row, col + 1, row_high, row_base, col_high, col_base):
                return True
        table[row][col] = "U"  # same with LR.
        table[row+1][col] = "D"

    else:
        if checker(table, row, col):
            return game_solver(table, row, col + 1, row_high, row_base, col_high, col_base)
        return False


def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with open(input_file, 'r') as input_file:
        row_high, row_base, col_high, col_base, table = input_initialization(input_file)

    with open(output_file, 'w') as output_file:
        if game_solver(table, 0, 0, row_high, row_base, col_high, col_base):
            for row in table:
                output_file.write(" ".join(map(str, row)))
                output_file.write("\n")
            output_file.seek(0, 2)  # pointing at the end of the file.
            end_position = output_file.tell()  # choosing that row.
            output_file.truncate(end_position - 1)  # deleting blank line at the end of the file.
        else:
            result = "No solution!"
            output_file.write(result)


if __name__ == '__main__':
    main()
