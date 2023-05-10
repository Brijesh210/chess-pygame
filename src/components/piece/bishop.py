from ..figure import Figure
import pygame


class Bishop(Figure):
    def __init__(self, color, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.color = color

        if color == (255, 255, 255):
            img = pygame.image.load("resources\\bishop_white.png")
        elif color == (0, 0, 0):
            img = pygame.image.load("resources\\bishop_black.png")

        img = pygame.transform.scale(img, (60, 64))
        self.img = img

    def canMove(self, removed_figure, new_pos_x, new_pos_y, figures):
        if abs(new_pos_x - self.pos_x) == abs(new_pos_y - self.pos_y):
            return True
        else:
            return False
