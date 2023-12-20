import pygame
import random

import Sudoko_Code
import Square
import Specifications


class Utilities:
    # select square
    @staticmethod
    def select_quare(squares, position):
        for i in range(9):
            for j in range(9):
                if squares[i][j].rect.collidepoint(position) and squares[i][j].color != Specifications.dark_gray:
                    return i, j
        return None

    # screens
    @staticmethod
    def main_menu_screen(easy, medium, hard):
        # background
        Specifications.display_surface.fill((54, 57, 69))
        # title
        title = Specifications.title_font.render("Sudoko", True, (255, 255, 255), None)
        title_rect = title.get_rect()
        title_rect.centerx = Specifications.width // 2
        title_rect.centery = easy.pos_y // 2
        Specifications.display_surface.blit(title, title_rect)
        # buttons
        easy.draw_all()
        medium.draw_all()
        hard.draw_all()

    @staticmethod
    def game_screen(check_button, solve_button):
        # fill the screen with a color
        Specifications.display_surface.fill((54, 57, 69))
        # check and solve buttons
        check_button.draw_all()
        solve_button.draw_all()

    # update, reset, check, and solve board
    @staticmethod
    def update(squares):
        for i in range(9):
            for j in range(9):
                # set text
                squares[i][j].text = squares[i][j].set_text(Specifications.copy_board)
                squares[i][j].display_text = squares[i][j].set_display_text()

                # display text
                squares[i][j].draw_rect()
                squares[i][j].draw_text()

    @staticmethod
    # reset
    def reset(squares):
        for i in range(len(squares)):  # iterate rows
            for j in range(len(squares[i])):  # iterate columns
                if Specifications.board[i][j] == 0:
                    squares[i][j].color = Specifications.light_gray
                    squares[i][j].text = squares[i][j].set_text(Specifications.board)
                    squares[i][j].display_text = squares[i][j].set_display_text()
                    Specifications.copy_board[i][j] = Specifications.board[i][j]
                squares[i][j].draw_all()

    @staticmethod
    # check button
    def check(squares, board):
        solved = True
        for i in range(len(board)):  # iterate rows
            for j in range(len(board[i])):  # iterate columns
                if squares[i][j].font_color == Specifications.font_color:  # if the square is not a pre-defined square
                    check_func = Sudoko_Code.checkValid(i, j, board[i][j], board)
                    if board[i][j] != 0 and not check_func:  # if the check function returns false
                        squares[i][j].color = Specifications.red
                        solved = False
                    elif board[i][j] == 0:
                        solved = False
                    elif check_func:
                        squares[i][j].color = Specifications.light_gray
        return solved

    @staticmethod
    # solve the board
    def solve(board, squares):
        while True:
            # uncomment to run slower
            # if time.time() % 1 == 0.5 or time.time() % 1 == 0:
            pygame.display.flip()
            temp = Sudoko_Code.empty(board)  # sets temp tuple to return of empty
            if temp:  # checks if temp is not None
                row, col = temp
            else:
                return True  # if temp is None then board is complete

            for i in range(1, len(board) + 1):  # iterator to go through each possible input for empty spot
                if Sudoko_Code.checkValid(row, col, i, board):  # checks if i is a valid input for space
                    board[row][col] = i  # sets the empty space to i
                    squares[row][col].text = str(i)
                    squares[row][col].display_text = squares[row][col].set_display_text()
                    squares[row][col].draw_text()
                    if Utilities.solve(board, squares):  # recursively calls itself to check each empty spot and backtrack if necessary
                        return True
                    board[row][col] = 0  # resets spot to empty if solve() returns false
                    squares[row][col].text = str(i)
                    squares[row][col].draw_rect()

            return False  # if checkValid() cannot find a valid number to fill spot, line 25 will execute

    # green out the board
    @staticmethod
    def green_out_board(squares):
        for i in range(9):
            for j in range(9):
                Specifications.board[i][j] = 0
                squares[i][j].font_color = (0, 0, 0)
                squares[i][j].display_text = squares[i][j].set_display_text()
                squares[i][j].color = Specifications.green

                squares[i][j].draw_rect()
                squares[i][j].draw_text()

    # make board methods
    @staticmethod
    def random_board(difficulty):
        total_filled = 0
        match difficulty:
            case 'easy':
                total_filled = 35
            case 'medium':
                total_filled = 26
            case 'hard':
                total_filled = 19
            case _:
                return [[0 for _ in range(9)] for _ in range(9)]

        while True:
            board = [[0 for _ in range(9)] for _ in range(9)]
            count = 0

            while count < total_filled:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
                value = random.randint(1, 9)
                if board[row][col] != 0: # check if the current position is filled
                    continue

                if Sudoko_Code.checkValid(row, col, value, board):
                    board[row][col] = value
                    count += 1

            passBoard = [[j for j in i] for i in board]
            if Sudoko_Code.solve(passBoard): # make sure the board is solvable
                return board

    @staticmethod
    def make_boards(easy, medium, hard, position):
        difficulty = ''
        if easy.rect.collidepoint(position):
            difficulty = 'easy'
        elif medium.rect.collidepoint(position):
            difficulty = 'medium'
        elif hard.rect.collidepoint(position):
            difficulty = 'hard'
        return_board = [[j for j in i] for i in Utilities.random_board(difficulty)]
        copy_return_board = [[j for j in i] for i in return_board]
        return return_board, copy_return_board

    @staticmethod
    def make_squares():
        squares = []
        pos_x = 20
        pos_y = 20
        for i in range(9):
            row = []
            for j in range(9):
                if j == 3 or j == 6:  # change x position by 5
                    pos_x += 5
                row.append(
                    Square.Square(50, 55, pos_x, pos_y, Specifications.light_gray, Specifications.default_font, '0', i, j))  # change x position by 49    # change x position by 49
                pos_x += 49
            if i == 2 or i == 5:  # change y position by 5
                pos_y += 5
            squares.append(row)
            pos_y += 54  # change y position by 54
            pos_x = 20  # change x position to 20

        return squares

    # draw the squares
    @staticmethod
    def draw_all(squares):
        for i in range(9):
            for j in range(9):
                squares[i][j].draw_rect()
                squares[i][j].draw_tect()
