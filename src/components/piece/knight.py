from ..figure import Figure
import pygame


class Knight(Figure):
    def __init__(self, color, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.color = color

        if color == "White":
            self.img = pygame.image.load("resources\\knight_white.png")
        elif color == "Black":
            self.img = pygame.image.load("resources\\knight_black.png")

        self.img = pygame.transform.scale(self.img, (60, 64))

    def canMove(self, removed_figure, new_pos_x, new_pos_y, figures):
        if (
            0 <= new_pos_x <= 7
            and (new_pos_x == self.pos_x - 2 or new_pos_x == self.pos_x + 2)
            and (new_pos_y == self.pos_y - 1 or new_pos_y == self.pos_y + 1)
        ):
            return True

        if (
            0 <= new_pos_y <= 7
            and (new_pos_y == self.pos_y - 2 or new_pos_y == self.pos_y + 2)
            and (new_pos_x == self.pos_x - 1 or new_pos_x == self.pos_x + 1)
        ):
            return True

        else:
            return False
