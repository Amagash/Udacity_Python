# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the input is square and contains at
# least one row and column.

correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]


incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]
print incorrect3[2][1]
incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]

incorrect6 = [[1, 2],
              [1, 2, 3]]

def is_square (sudoku):
    nbr_lines = len(sudoku)
    for e in sudoku:
        if len(e) != nbr_lines:
            return False
    return True

def is_int (sudoku):
    for line in sudoku:
        for e in line:
            if not type(e) is int:
                return False
    return True

def rows_check(sudoku):
    for line in sudoku:
        for e in line:
            i = 0
            occurence = 0
            while i < len(line):
                if e == line[i]:
                    occurence = occurence + 1
                i = i + 1
            if occurence > 1:
                return False
    return True


def col_check(sudoku):
    col = []
    i = 0
    while i < len(sudoku):
        index = []
        for row in sudoku:
            index.append(row[i])
        i = i + 1
        col.append(index)


    for line in col:
        for e in line:
            liste = []
            i = 0
            occurence = 0
            while i < len(line):
                if e == line[i]:
                    occurence = occurence + 1
                i = i + 1
            if occurence > 1:
                return False
    return True


def whole_numbers_check(sudoku):
    for line in sudoku:
        for e in line:
            if not 1 <= e <= len(line):
                return False
    return True

def check_sudoku(sudoku):
    if is_int(sudoku) != True:
        return False
    if is_square(sudoku) != True:
        return False
    if whole_numbers_check(sudoku) != True:
        return False
    if rows_check(sudoku) == True and col_check(sudoku) == True:
        return True
    else:
        return False

print check_sudoku(incorrect)
# # >>> False
#
print check_sudoku(correct)
# # >>> True

print check_sudoku(incorrect2)
# >>> False

print check_sudoku(incorrect3)
# >>> False

print check_sudoku(incorrect4)
# >>> False

print check_sudoku(incorrect5)
# >>> False

print check_sudoku(incorrect6)
# # >>> False



