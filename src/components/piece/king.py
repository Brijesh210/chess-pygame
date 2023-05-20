from ..figure import Figure
import pygame


class King(Figure):
    def __init__(self, color, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.color = color

        if color == "White":
            img = pygame.image.load("resources\\king_white.png")
        elif color == "Black":
            img = pygame.image.load("resources\\king_black.png")

        img = pygame.transform.scale(img, (60, 64))
        self.img = img

    def canMove(self, removed_figure, new_pos_x, new_pos_y, figures):

        if 0 <= new_pos_x <= 7 and self.pos_x - 1 <= new_pos_x <= self.pos_x + 1:
            if 0 <= new_pos_y <= 7 and self.pos_y - 1 <= new_pos_y <= self.pos_y + 1:
                return True
        else:
            return False
