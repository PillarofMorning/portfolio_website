p = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sudoku = [[8, 7, 6, 9, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 6, 0, 0, 0],
          [0, 4, 0, 3, 0, 5, 8, 0, 0],
          [4, 0, 0, 0, 0, 0, 2, 1, 0],
          [0, 9, 0, 5, 0, 0, 0, 0, 0],
          [0, 5, 0, 0, 4, 0, 3, 0, 6],
          [0, 2, 9, 0, 0, 0, 0, 0, 8],
          [0, 0, 4, 6, 9, 0, 1, 7, 3],
          [0, 0, 0, 0, 0, 1, 0, 0, 4]]


def possibilities(puzzle, row, column):

    c = column - column % 3
    r = row - row % 3

    grid = [x for x in puzzle[row] if not isinstance(x, list)]
    solver(grid, puzzle, row, column)

    grid = [puzzle[x][column] for x in range(len(sudoku))]
    solver(grid, puzzle, row, column)

    grid = [puzzle[i + c][j + r] for j in range(3) for i in range(3)]
    solver(grid, puzzle, row, column)


def solver(grid, puzzle, row, column):
    for number in grid:
        if not isinstance(sudoku[row][column], list):
            continue
        elif number in sudoku[row][column]:
            sudoku[row][column].pop(sudoku[row][column].index(number))
            if len(sudoku[row][column]) == 1:
                sudoku[row][column] = sudoku[row][column][0]
    return

def board_setup():
    for row_number in range(len(sudoku)):
        for number in range(len(sudoku[row_number])):
            if sudoku[row_number][number] == 0:
                sudoku[row_number][number] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

board_setup()

state = 'false'
while state == 'false':
    for row_number in range(len(sudoku)):
        for number in range(len(sudoku[row_number])):
            if isinstance(sudoku[row_number][number], list) and len(sudoku[row_number][number]) > 1:
                possibilities(sudoku, row_number, number)

    sudo_state = []
    for a in sudoku:
        if any(isinstance(x, list) for x in a):
            sudo_state.append('false')
        else:
            sudo_state.append('true')

    if 'false' in sudo_state:
        state = 'false'
    else:
        state = 'true'


print('yella')
for x in sudoku:
    print(x)