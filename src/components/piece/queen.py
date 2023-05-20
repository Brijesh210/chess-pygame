from ..figure import Figure
import pygame


class Queen(Figure):
    def __init__(self, color, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.color = color

        if color == "White":
            self.img = pygame.image.load("resources\\queen_white.png")
        elif color == "Black":
            self.img = pygame.image.load("resources\\queen_black.png")

        self.img = pygame.transform.scale(self.img, (60, 64))

    def canMove(self, removed_figure, new_pos_x, new_pos_y, board_pos):
        if self.pos_x == new_pos_x:
            current_step = new_pos_y if self.pos_y > new_pos_y else self.pos_y
            max_step = self.pos_y if self.pos_y > new_pos_y else new_pos_y

            while current_step + 1 < max_step:
                if board_pos[self.pos_x][current_step + 1] is not None:
                    return False

                current_step = current_step + 1

            return True

        if self.pos_y == new_pos_y:
            current_step = new_pos_x if self.pos_x > new_pos_x else self.pos_x
            max_step = self.pos_x if self.pos_x > new_pos_x else new_pos_x

            while current_step + 1 < max_step:
                if board_pos[current_step + 1][new_pos_y] is not None:
                    return False

                current_step = current_step + 1

            return True

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

       
        return False
