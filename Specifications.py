import pygame

import Sudoko_Code

# window settings
# basic pygame settings
pygame.init()
width = 490
height = 755
display_surface = pygame.display.set_mode((width, height))
display_surface.fill((60, 63, 65))
pygame.display.set_caption('Sudoko')
clock = pygame.time.Clock()
default_font = pygame.font.Font('freesansbold.ttf', 40)
title_font = pygame.font.Font("/Users/tannersmith/opt/anaconda3/lib/python3.8/site-packages/pygame/Preahvihear-Regular.ttf", 80)
button_font = font = pygame.font.Font('freesansbold.ttf', 25)
font_color = (92, 130, 160)

# colors
red = (255, 105, 105)
dark_gray = (190, 190, 190)  # un-editable color
light_gray = (230, 230, 230)  # editable color
flashing_color = (185, 185, 185)
green = (95, 153, 92)

# board
board = [[j for j in i] for i in Sudoko_Code.board]
copy_board = [[j for j in i]for i in board]
solve_board = [[j for j in i]for i in board]




