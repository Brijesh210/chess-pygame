from ..figure import Figure
import pygame


class Pawn(Figure):
    def __init__(self, color, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.color = color
        if color == (255, 255, 255):
            img = pygame.image.load("resources\\pawn_white.png")
        elif color == (0, 0, 0):
            img = pygame.image.load("resources\\pawn_black.png")

        img = pygame.transform.scale(img, (60, 64))
        self.img = img

    def canMove(self, removed_figure, new_pos_x, new_pos_y, figures):

        if self.color == (255, 255, 255):
            if new_pos_y == self.pos_y - 1:
                if (
                    0 <= new_pos_x <= 7
                    and self.pos_x - 1 <= new_pos_x <= self.pos_x + 1
                ):
                    if removed_figure is not None:
                        if (
                            removed_figure.pos_y == self.pos_y - 1
                            and removed_figure.pos_x == self.pos_x
                        ):
                            return False
                    return True
        elif self.color == (0, 0, 0):
            if new_pos_y == self.pos_y + 1:
                if (
                    0 <= new_pos_x <= 7
                    and self.pos_x - 1 <= new_pos_x <= self.pos_x + 1
                ):
                    if removed_figure is not None:
                        if (
                            removed_figure.pos_y == self.pos_y + 1
                            and removed_figure.pos_x == self.pos_x
                        ):
                            return False
                    return True

        else:
            return False
