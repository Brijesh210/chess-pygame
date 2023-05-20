from ..figure import Figure
import pygame


class Pawn(Figure):
    def __init__(self, color, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.color = color
        self.first_move = True
        if color == "White":
            self.img = pygame.image.load("resources\\pawn_white.png")
        elif color == "Black":
            self.img = pygame.image.load("resources\\pawn_black.png")

        self.img = pygame.transform.scale(self.img, (60, 64))

    def canMove(self, removed_figure, new_pos_x, new_pos_y, figures):
        if self.color == "White":
            if new_pos_y == self.pos_y - 1 or (
                new_pos_y == self.pos_y - 2 and self.first_move == True
            ):
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
                    self.first_move = False
                    return True

        elif self.color == "Black":
            if new_pos_y == self.pos_y + 1 or (
                new_pos_y == self.pos_y + 2 and self.first_move == True
            ):
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
                    self.first_move = False
                    return True

        else:
            return False
