import sys


def turn_to_dictionary(game_str):  # every number marked starting 1 to n
    table = {}
    for i, line in enumerate(game_str, start=1):
        elements = line.split()
        for j, element in enumerate(elements, start=1):
            table[(i, j)] = (int(element))  # used int() for scoring
    return table


def turn_to_string(table):
    max_row = max(row for row, _ in table) if table else 0  # finding maximum row and col if exist
    max_col = max(col for _, col in table) if table else 0

    result = ""
    for row in range(1, max_row + 1):
        row_values = [table.get((row, col), ' ') for col in range(1, max_col + 1)]  # getting all values into a list
        row_str = ' '.join(str(value) if value != ' ' else ' ' for value in row_values)  # that list turning to string
        result += row_str + "\n"

    return result


def input_check(table):
    row, col = map(int, input("Please enter a row and a column number: ").split())
    if (row, col) in table:
        return row, col
    else:
        print("\nPlease enter a correct size!\n")
        return input_check(table)


def move_algorithm(table, row, col, num):
    if table[(row, col)] == ' ':
        return False
    else:
        selected_cells = set()

        def neighbors(r, c, value):
            if (r, c) not in selected_cells and (r, c) in table and table[(r, c)] == value:
                selected_cells.add((r, c))
                neighbors(r - 1, c, value)  # above
                neighbors(r + 1, c, value)  # below
                neighbors(r, c - 1, value)  # left
                neighbors(r, c + 1, value)  # right

        neighbors(row, col, num)

        if len(selected_cells) > 1:
            score = num * len(selected_cells)
            for cell in selected_cells:
                table[cell] = ' '
            selected_cells.clear()
            shift_down_algorithm(table)  # cleared and shifting
            shift_left_algorithm(table)
            shift_up_algorithm(table)
            return score
        else:
            selected_cells.clear()
            return 0  # return 0 as score


def shift_down_algorithm(table):
    # shift downward
    for r in range(max(row for row, _ in table), 0, -1):
        for c in range(1, max(col for _, col in table) + 1):
            current_cell = (r, c)
            if table[current_cell] == ' ':
                for above in range(r - 1, 0, -1):
                    above_cell = (above, c)
                    if table[above_cell] != ' ' and table[current_cell] == ' ':
                        table[current_cell] = table[above_cell]
                        table[above_cell] = ' '
                        break


def shift_up_algorithm(table):
    max_row = max(row for row, _ in table)
    max_col = max(col for _, col in table)
    while all((1, c) in table and table[(1, c)] == ' ' for c in range(1, max_col + 1)):
        for r in range(1, max_row):
            for c in range(1, max_col + 1):
                current_cell = (r, c)
                below_cell = (r + 1, c)
                table[current_cell] = table[below_cell]
                table[below_cell] = ' '

        # Remove the empty row at the bottom
        for c in range(1, max_col + 1):
            bottom_cell = (max_row, c)
            del table[bottom_cell]


def shift_left_algorithm(table):
    for col in range(1, max(col for _, col in table)):
        column_empty = all(table[(row, col)] == ' ' for row in range(1, max(row for row, _ in table) + 1))
        if column_empty:
            for r in range(1, max(row for row, _ in table) + 1):
                table[(r, col)] = table[(r, col + 1)]
                table[(r, col + 1)] = ' '


def check_game_over(table):
    if all(value == ' ' for value in table.values()) or not any(table.values()):
        return True

    for row in range(1, max(r for r, _ in table) + 1):
        for col in range(1, max(c for _, c in table) + 1):
            current_cell = (row, col)
            current_value = table.get(current_cell)

            # Skip cells with no value
            if current_value is None or current_value == ' ':
                continue

            # Check if there are adjacent cells with the same value
            neighbors = [
                (row - 1, col),  # above
                (row + 1, col),  # below
                (row, col - 1),  # left
                (row, col + 1),  # right
            ]

            for neigh_cell in neighbors:
                if neigh_cell in table and table[neigh_cell] == current_value:
                    return False  # Game is not over. Still have moves.

    return True  # No adjacent cells with the same value, game over


def game_algorithm(table):
    score = 0

    if not table:
        print("Game over.")
        sys.exit(1)

    while True:  # recursive function
        if check_game_over(table):
            print(f"Your score is: {score}\n")
            print("Game over")
            break

        print(f"Your score is: {score}\n")
        row, col = input_check(table)
        num = table[(row, col)]
        move_result = move_algorithm(table, row, col, num)

        if not move_result:
            print("\nNo movement happened try again\n")
            print(turn_to_string(table))
        else:
            score += move_result
            print()
            print(turn_to_string(table))


def main():
    with open("input.txt", "r") as input_file:
        game_str = input_file.read().strip().split("\n")
    table = turn_to_dictionary(game_str)
    print(turn_to_string(table))
    game_algorithm(table)


if __name__ == "__main__":
    main()
