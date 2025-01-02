import sys


def check(matrix, row, col, val):

    for x in range(9):  # The numbers in the same row were checked.
        if matrix[row][x] == val:
            return False

    for x in range(9):  # The numbers in the same column were checked.
        if matrix[x][col] == val:
            return False

    first_row = row - row % 3  # The numbers in 3x3 grid were checked.
    first_col = col - col % 3
    for a in range(3):
        for b in range(3):
            if matrix[a + first_row][b + first_col] == val:
                return False

    return True


def possibility(matrix, row, col):  # Possibilities in the grid are found and counted.
    possibilities = []
    for val in range(1, 10):
        if check(matrix, row, col, val):
            possibilities.append(val)
    return possibilities


def priority(matrix2):  # Cells with a single possible value are prioritized, starting from the top-left.

    for row in range(9):
        for col in range(9):
            if matrix2[row][col] == 0:
                possibilities = possibility(matrix2, row, col)
                if len(possibilities) == 1:
                    return row, col, possibilities[0]

    return None


def matrix_to_string(matrix):  # 2D matrix was turned string.

    solved_sudoku = ""
    for row in matrix:
        row_str = ""
        for val in row:
            row_str = row_str + str(val) + ' '
        solved_sudoku = solved_sudoku + row_str.strip() + "\n"
    return solved_sudoku.strip()


def is_it_finished(matrix):
    empty_cells = 0
    for row in range(9):
        for col in range(9):
            if matrix[row][col] == 0:
                empty_cells += 1
    if empty_cells == 0:
        return True
    else:
        return False


def solver(matrix, row, col, output_file, step_counter):
    if is_it_finished(matrix):
        output_file.write("------------------")
        print("Sudoku solved in output.txt.")
        sys.exit(1)
    if col == 9:  # Skipped next row when column was finished.
        row += 1
        col = 0

    if row == 9:  # All rows checked. Code finished.
        return True

    selected_cell = priority(matrix)  # Cell was chosen by priority rules
    if selected_cell:  # If a cell with only one possibility is found, its solved.
        row, col, val = selected_cell
        matrix[row][col] = val
        step_counter += 1

        output = ("Step " + str(step_counter) + " - " + str(val)
                  + " @ R" + str(row + 1) + "C" + str(col + 1) + "\n")
        output_file.write("------------------\n")
        output_file.write(output)
        output_file.write("------------------\n")
        output_file.write(matrix_to_string(matrix) + '\n')
        return solver(matrix, row, col + 1, output_file, step_counter)

    for val in range(1, 10):  # Values in the range from 1 to 9 are checked if there is no special condition.

        matrix[row][col] = 0
        if check(matrix, row, col, val):
            matrix[row][col] = val
            step_counter += 1

            output = ("Step " + str(step_counter) + " - " + str(val)
                      + " @ R" + str(row + 1) + "C" + str(col + 1) + "\n")
            output_file.write("------------------\n")
            output_file.write(output)
            output_file.write("------------------\n")
            output_file.write(matrix_to_string(matrix) + '\n')

            if solver(matrix, row, col + 1, output_file, step_counter):
                return True

    if matrix[row][col] != 0:  # Code returned to the next column.
        return solver(matrix, row, col + 1, output_file, step_counter)

    return False


def main():

    input_file = open("input.txt", "r")
    output_file = open("output.txt", "w")

    sudoku_str = input_file.read().strip()
    sudoku_int = []
    for line in sudoku_str.split('\n'):
        for number in line.split():
            sudoku_int.append(int(number))

    if len(sudoku_int) != 81:  # If the input doesn't a valid 9x9 grid.
        print("you must have 9x9 sudoku")
        sys.exit(1)

    matrix = []  # The given sudoku list turned 9x9 matrix.
    for i in range(0, 81, 9):
        matrix.append(sudoku_int[i:i + 9])

    step_counter = 0
    if solver(matrix, 0, 0, output_file, step_counter):
        output_file.write("------------------")
        print("Sudoku solved in output.txt.")

    else:
        print("No solution for given sudoku in input.txt")

    input_file.close()  # The file was closed
    output_file.close()  # The file was closed


if __name__ == "__main__":
    main()
