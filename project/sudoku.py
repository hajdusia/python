#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from string import upper
from sys import argv

LETTERS = range(ord('A'), ord('J'))
CSI = "\x1B["

sudoku = [
    [1, 2, 3, 6, 7, 8, 9, 4, 5],
    [5, 8, 4, 2, 3, 9, 7, 6, 1],
    [9, 6, 7, 1, 4, 5, 3, 2, 8],
    [3, 7, 2, 4, 6, 1, 5, 8, 9],
    [6, 9, 1, 5, 8, 3, 2, 7, 4],
    [4, 5, 0, 7, 9, 2, 6, 1, 3],
    [8, 3, 6, 9, 2, 4, 1, 5, 7],
    [2, 1, 9, 8, 5, 7, 4, 3, 6],
    [7, 4, 5, 3, 1, 6, 8, 9, 0]
]


def load_game():
    os.system('clear')
    print "Select the board number (between 1 and 50 required)."
    board_number = int(
        raw_input("Note that first board is the easiest one just to demonstrate how the program works: "))

    pathname = os.path.dirname(sys.argv[0])
    fullpath = os.path.abspath(pathname)

    if 1 <= board_number <= 50:
        sudokus = open(fullpath + '/sudoku.txt', 'r')
        sudoku = sudokus.readlines()[board_number - 1]

        sudoku = list(list(sudoku)[i * 9:i * 9 + 9] for i in range(0, 9))
        return map(lambda row: map(lambda point: int(point), row), sudoku)
    else:
        load_game()


def colour_str(x, fg, bg):
    return CSI + str(fg) + ";" + str(bg) + "m" + str(x) + CSI + "0m"


def print_sudoku(sudoku):
    os.system('clear')
    print '      ' + '   '.join(map(lambda x: str(x), range(1, 10)))

    row_counter = 0
    for row in sudoku:
        print '    +---+---+---+---+---+---+---+---+---+'
        print ' ' + chr(LETTERS[row_counter]) + '  | ' + ' | '.join(
            map(lambda x: colour_str(x, 1, 0) if x != 0 else ' ', row)) + ' |'
        row_counter += 1
    print '    +---+---+---+---+---+---+---+---+---+\n'


def is_complete(sudoku):
    for row in sudoku:
        for point in row:
            if point == 0:
                return False
    return True


def read_value():
    while True:
        input = raw_input("Insert value [1-9]: ")
        if input in map(lambda x: chr(x), range(ord('1'), ord('9') + 1)):
            return int(input)
        else:
            print "Invalid input '" + input + "' for value (character between '1' and '9' required)!"


def read_coordinates():
    while True:
        input = raw_input("Insert coordinates [A1-I9]: ")
        if len(input) == 2:
            x_coord = input[0]
            y_coord = input[1]
            if not (upper(x_coord) in map(lambda x: chr(x), range(ord('A'), ord('I') + 1))):
                print "Invalid input '" + x_coord + "' for row (character between 'A' and 'I' required)!"
            elif not (y_coord in map(lambda x: chr(x), range(ord('1'), ord('9') + 1))):
                print "Invalid input '" + y_coord + "' for column (character between '1' and '9' required)!"
            else:
                return (ord(upper(x_coord)) - ord('A'), upper(x_coord)), (int(y_coord) - 1, y_coord)
        else:
            print "Invalid coordinates!"


def can_change_field(sudoku, x, y):
    return sudoku[x][y] == 0


def check_board(sudoku):
    for row in sudoku:
        if set(row) != set(range(1, 10)):
            return False
    for i in range(0, 9):
        column = map(lambda row: row[i], sudoku)
        if set(column) != set(range(1, 10)):
            return False
    for square_x in range(0, 3):
        for square_y in range(0, 3):
            values = set()
            for x in range(0, 3):
                for y in range(0, 3):
                    values.add(sudoku[square_x * 3 + x][square_y * 3 + y])
            if set(values) != set(range(1, 10)):
                return False
    return True


def play(sudoku):
    start = list(sudoku)

    while not is_complete(sudoku):
        ((x, pos_x), (y, pos_y)) = read_coordinates()

        if not can_change_field(start, x, y):
            print pos_x + pos_y, "cannot be modified!"
            continue

        value = read_value()
        sudoku[x][y] = value
        print_sudoku(sudoku)

        print "Success, value:", value, "added to", pos_x + pos_y

    if check_board(sudoku):
        print "Verification in progress... " + colour_str('GOOD', 32, 0)
    else:
        print "Verification in progress... " + colour_str('WRONG', 31, 0)


if __name__ == '__main__':
    if len(argv) == 2 and argv[1] in ('-h', '--help'):
        print "Sudoku is a logic-based, combinatorial number-placement puzzle."
        print "The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid contains all of the digits from 1 to 9."
        print "The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution."
        print ""
        print "Setup:"
        print "To properly run the program, the sudoku.sh and sudoku.txt files should be placed in the same directory."
        exit(0)
    else:
        sudoku = load_game()
        print_sudoku(sudoku)
        play(sudoku)
