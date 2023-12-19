# sudoko solver using backtracking

import pygame.time

clock = pygame.time.Clock()
board = [[0, 7, 0, 0, 0, 8, 0, 0, 0],
         [0, 0, 0, 0, 0, 9, 7, 4, 0],
         [8, 4, 0, 2, 0, 0, 0, 6, 0],
         [1, 0, 0, 0, 0, 6, 0, 0, 0],
         [3, 9, 0, 0, 0, 0, 0, 8, 5],
         [0, 0, 0, 3, 0, 0, 0, 0, 1],
         [0, 2, 0, 0, 0, 4, 0, 9, 3],
         [0, 5, 8, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 5, 0, 0, 0, 1, 0]]


def solve(board):
    temp = empty(board)  # sets temp tuple to return of empty
    if temp:  # checks if temp is not None
        row, col = temp
    else:
        return True  # if temp is None then board is complete

    for i in range(1, len(board) + 1):  # iterator to go through each possible input for empty spot
        if checkValid(row, col, i, board):  # checks if i is a valid input for space
            board[row][col] = i  # sets the empty space to i
            #print(row, col, i)
            if solve(board):  # recursively calls itself to check each empty spot and backtrack if necessary
                return True
            #print('wrong', row, col, i)
            board[row][col] = 0  # resets spot to empty if solve() returns false
        #else:
        #print('invalid', row, col, i)

    return False  # if checkValid() cannot find a valid number to fill spot, line 25 will execute


def empty(board):  # looks for first empty spot
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j


def checkValid(row, col, val, board):
    # check box for duplicate number
    for i in range((row // 3) * 3, ((row // 3) * 3) + 3):
        for j in range((col // 3) * 3, ((col // 3) * 3) + 3):
            if board[i][j] == val and (i, j) != (row, col):
                return False

    # check row for duplicate number
    for i in range(len(board[row])):
        if board[row][i] == val and i != col:
            return False

    # check column for duplicate number
    for i in range(len(board[row])):  # use len(board[row]) b/c of symmetry of board
        if board[i][col] == val and i != row:
            return False

    return True





