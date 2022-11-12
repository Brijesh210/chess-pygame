import math
from ..figure import Figure
import pygame


class Queen(Figure):
    def __init__(self, color, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.color = color

        if color == (255, 255, 255):
            img = pygame.image.load("res\\queen_white.png")
        elif color == (0, 0, 0):
            img = pygame.image.load("res\\queen_black.png")

        img = pygame.transform.scale(img, (60, 64))
        self.img = img

    def canMove(self, removed_figure, new_pos_x, new_pos_y):
        if 0 <= new_pos_x <= 7 and new_pos_y == self.pos_y:
            return True
        elif 0 <= new_pos_y <= 7 and new_pos_x == self.pos_x:
            return True
        elif abs(new_pos_x - self.pos_x) == abs(new_pos_y - self.pos_y):
            return True
        else:
            return False
