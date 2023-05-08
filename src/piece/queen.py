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

    # TODO rook, bishop
    def canMove(self, removed_figure, new_pos_x, new_pos_y, figures):

        if (
            0 <= new_pos_x <= 7
            and new_pos_y == self.pos_y
            or 0 <= new_pos_y <= 7
            and new_pos_x == self.pos_x
            or abs(new_pos_x - self.pos_x) == abs(new_pos_y - self.pos_y)
        ):
            for i in range(min(self.pos_x, new_pos_x) + 1, max(self.pos_x, new_pos_x)):
                print("hell_y_same = " + str(i))
                if figures[i][self.pos_y] is not None:
                    print("false here = y ")
                    print(figures[self.pos_x][j])
                    return False

            for j in range(min(self.pos_y, new_pos_y) + 1, max(self.pos_y, new_pos_y)):
                print("hell_x_same= " + str(j))

                if figures[self.pos_x][j] is not None:
                    print("false here = x")
                    print(figures[self.pos_x][j])
                    return False

            x_dir = -1 if new_pos_x < self.pos_x else 1
            y_dir = -1 if new_pos_y < self.pos_y else 1
            for i, j in zip(
                range(self.pos_x + x_dir, new_pos_x, x_dir),
                range(self.pos_y + y_dir, new_pos_y, y_dir),
            ):
                if figures[i][j] is not None:
                    return False

            return True

        else:
            return False
