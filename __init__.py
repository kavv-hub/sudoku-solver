def solve(sudoku):
    empty_locations = find_empty(sudoku)
    if len(empty_locations) == 0:
        return

    i = 0
    while i < len(empty_locations):
        row, col = empty_locations[i]
        value = get_value(sudoku, row, col)
        if value is not None:
            sudoku[row][col] = value
            i += 1
        else:
            sudoku[row][col] = 0
            i = get_previous_index(i, empty_locations)

    for row in sudoku:
        print(row)


def find_empty(sudoku):
    locations = []
    for row in range(len(sudoku)):
        for col in range(len(sudoku[row])):
            if sudoku[row][col] == 0:
                locations.append([row, col])
    return locations


def get_previous_index(current, list):
    if current == 0:
        return len(list) - 1
    return current - 1


def get_value(sudoku, row, col):
    for value in range(sudoku[row][col] + 1, 10):
        if is_valid(sudoku, row, col, value):
            return value
    return None


def is_valid(sudoku, row, col, target):
    return used_in_box(sudoku, row - row % 3, col - col % 3, target) == 0 \
           and used_in_row(sudoku, row, target) == 0 \
           and used_in_col(sudoku, col, target) == 0


def used_in_row(sudoku, row, target):
    count = 0
    for col in range(9):
        if sudoku[row][col] == target:
            count += 1
    return count


def used_in_col(sudoku, col, target):
    count = 0
    for row in range(9):
        if sudoku[row][col] == target:
            count += 1
    return count


def used_in_box(sudoku, r_offset, c_offset, target):
    count = 0
    for row in range(3):
        for col in range(3):
            if sudoku[row + r_offset][col + c_offset] is target:
                count += 1
    return count


if __name__ == "__main__":
    # this is an example
    solve([
        [5, 6, 0, 0, 0, 0, 0, 0, 3],
        [0, 4, 0, 0, 0, 1, 0, 0, 7],
        [0, 9, 0, 0, 3, 8, 2, 0, 0],
        [6, 8, 5, 0, 2, 0, 0, 0, 0],
        [0, 3, 0, 5, 8, 9, 0, 0, 0],
        [0, 0, 9, 0, 4, 0, 5, 0, 8],
        [4, 7, 3, 2, 0, 0, 0, 9, 0],
        [0, 0, 0, 3, 9, 0, 0, 2, 0],
        [9, 0, 6, 8, 0, 0, 3, 4, 0]
    ])