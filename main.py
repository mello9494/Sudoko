import pygame
import time
from sys import exit

import Sudoko_Code
import Square
import Utilities
import Specifications


def main():
    # flags for each screen
    main_menu_screen, game_screen, new_game_screen = True, False, False
    # flag for checking if square is selected
    active = False
    row, col = -1, -1
    tick = 60
    # initializing classes
    utilities = Utilities.Utilities
    window = Utilities.Utilities
    buttons = Square.Button
    # initializing buttons and squares
    easy, medium, hard = buttons.start_buttons()
    check_button, solve_button = buttons.check_and_solve()
    new_game = buttons.new_game_button()
    squares = utilities.make_squares()

    while True:
        # get event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            # mouse click detection
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                temp = utilities.select_quare(squares, position)
                if temp and game_screen: # only allow square-position checking during the game screen
                    row, col = temp
                    active = True

                # logic for each screen
                if main_menu_screen:
                    if easy.rect.collidepoint(position) or medium.rect.collidepoint(position) or hard.rect.collidepoint(position):
                        # make boards
                        Specifications.board, Specifications.copy_board = utilities.make_boards(easy, medium, hard, position)
                        Specifications.solve_board = [[j for j in i] for i in Specifications.board]
                        # solve the board
                        Sudoko_Code.solve(Specifications.solve_board)
                        # make the game screen
                        window.game_screen(check_button, solve_button)
                        # screen flags
                        main_menu_screen = False
                        game_screen = True
                elif game_screen:
                    if check_button.rect.collidepoint(position):
                        active = False
                        if utilities.check(squares, Specifications.copy_board):
                            # fill the squares with green to show correct
                            utilities.green_out_board(squares)
                            # draw new_game button
                            new_game.draw_all()
                            # screen flags
                            new_game_screen = True
                            game_screen = False
                    elif solve_button.rect.collidepoint(position):
                        active = False
                        # make the boards the original
                        utilities.reset(squares)
                        Specifications.copy_board = [[j for j in i] for i in Specifications.board]
                        # show the board being solved
                        utilities.solve(Specifications.copy_board, squares)
                        # fill the squares with green to show correct
                        utilities.green_out_board(squares)
                        # draw new_game button
                        new_game.draw_all()
                        # screen flags
                        new_game_screen = True
                        game_screen = False
                elif new_game_screen:
                    if new_game.rect.collidepoint(position): # resetting the game
                        # fill the screen with a color
                        Specifications.display_surface.fill(Specifications.dark_gray)
                        # make new squares
                        squares = utilities.make_squares()
                        # reset boards
                        Specifications.board = [[0 for _ in range(9)] for _ in range(9)]
                        Specifications.copy_board = [[0 for _ in range(9)] for _ in range(9)]
                        Specifications.solve_board = [[0 for _ in range(9)] for _ in range(9)]
                        row, col = -1, -1
                        # screen flags
                        new_game_screen = False
                        main_menu_screen = True

            # editing text
            if event.type == pygame.KEYDOWN:
                temp_text_box = ''
                if Specifications.copy_board[row][col] != 0:
                    temp_text_box = str(Specifications.copy_board[row][col])
                squares[row][col].edit_text(event, temp_text_box)

        # draw updates to screen
        if main_menu_screen:
            window.main_menu_screen(easy, medium, hard)
        elif game_screen:
            window.update(squares)

        # active square
        color = squares[row][col].color
        if active:  # flash box that is selected
            if time.time() % 1 > 0.5:
                color = squares[row][col].color
            else:
                color = Specifications.flashing_color

            # draw the flashing square
            pygame.draw.rect(Specifications.display_surface, color, squares[row][col].rect)
            pygame.draw.rect(Specifications.display_surface, (0, 0, 0), squares[row][col].rect, 1)  # draw the selected box with the updated color
            Specifications.display_surface.blit(squares[row][col].display_text, squares[row][col].display_text.get_rect(center=squares[row][col].rect.center))

        pygame.display.flip()
        Specifications.clock.tick(tick)


if __name__ == '__main__':
    main()