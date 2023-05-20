from ..figure import Figure
import pygame


class Bishop(Figure):
    def __init__(self, color, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.color = color

        if color == "White":
            self.img = pygame.image.load("resources\\bishop_white.png")
        elif color == "Black":
            self.img = pygame.image.load("resources\\bishop_black.png")

        self.img = pygame.transform.scale(self.img, (60, 64))

    def canMove(self, removed_figure, new_pos_x, new_pos_y, board_pos):
        if abs(new_pos_x - self.pos_x) == abs(new_pos_y - self.pos_y):
            x_dir = -1 if new_pos_x < self.pos_x else 1
            y_dir = -1 if new_pos_y < self.pos_y else 1
            for i, j in zip(
                range(self.pos_x + x_dir, new_pos_x, x_dir),
                range(self.pos_y + y_dir, new_pos_y, y_dir),
            ):
                if board_pos[i][j] is not None:
                    return False

            return True
        else:
            return False
