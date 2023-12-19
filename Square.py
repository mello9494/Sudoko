import pygame

import Specifications

pygame.init()


class Object:
    width = 0
    height = 0
    pos_x = 0
    pos_y = 0
    color = None
    font = Specifications.default_font
    rect = None
    text = ''
    display_text = None

    def __init__(self, width, height, pos_x, pos_y, color, font, text):
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.text = text
        self.font = font
        self.display_text = self.font.render(self.text, True, (0, 0, 0), None)
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

    def draw_text(self):
        Specifications.display_surface.blit(self.display_text, self.display_text.get_rect(center=self.rect.center))

    def draw_rect(self):
        pygame.draw.rect(Specifications.display_surface, self.color, self.rect)
        pygame.draw.rect(Specifications.display_surface, (0, 0, 0), self.rect, 1)

    def draw_all(self):
        self.draw_rect()
        self.draw_text()

class Square(Object):
    def __init__(self, width, height, pos_x, pos_y, color, font, text, row, col):
        super().__init__(width, height, pos_x, pos_y, color, font, text)
        self.row = row
        self.col = col
        self.font_color = Specifications.font_color
        self.text = self.set_text(Specifications.copy_board)
        self.display_text = self.set_display_text()

    def set_text(self, board):
        text = str(board[self.row][self.col])
        return text

    def set_display_text(self):
        if self.text == '0':
            text = self.font.render('', True, self.font_color, None)
        else:
            text = self.font.render(self.text, True, self.font_color, None)
        return text

    def draw_rect(self):
        if Specifications.board[self.row][self.col] != 0:
            self.color = Specifications.dark_gray
            self.font_color = (0, 0, 0)
        pygame.draw.rect(Specifications.display_surface, self.color, self.rect)
        pygame.draw.rect(Specifications.display_surface, (0, 0, 0), self.rect, 1)

    def edit_text(self, event, text):
        if event.key == pygame.K_BACKSPACE:
            if len(text) > 0:
                self.color = Specifications.light_gray
                text = ''
                Specifications.copy_board[self.row][self.col] = 0
        elif len(text) == 0 and pygame.K_1 <= event.key <= pygame.K_9:  # only accept numbers
            text += event.unicode
            text = text[0]
            Specifications.copy_board[self.row][self.col] = int(text[0])


class Button(Object):
    def __init__(self, width, height, pos_x, pos_y, color, font, text):
        super().__init__(width, height, pos_x, pos_y, color, font, text)

    @staticmethod
    def check_and_solve():
        check_button = Object(100, 50, 123, 550, Specifications.light_gray, Specifications.button_font, 'Check')
        solve_button = Object(100, 50, 285, 550, Specifications.light_gray, Specifications.button_font, 'Solve')

        return check_button, solve_button

    @staticmethod
    def start_buttons():
        easy = Object(80, 50, 50, 550, Specifications.light_gray, Specifications.button_font, 'Easy')
        medium = Object(120, 50, 180, 550, Specifications.light_gray, Specifications.button_font, 'Medium')
        hard = Object(80, 50, 350, 550, Specifications.light_gray, Specifications.button_font, 'Hard')
        return easy, medium, hard

    @staticmethod
    def new_game_button():
        new_game = Object(150, 50, 165, 650, Specifications.light_gray, Specifications.button_font, 'New Game')
        return new_game


