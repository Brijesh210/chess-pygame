from ..figure import Figure
import pygame


class King(Figure):
    def __init__(self, color, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.color = color

        if color == (255, 255, 255):
            img = pygame.image.load("res\\king_white.png")
        elif color == (0, 0, 0):
            img = pygame.image.load("res\\king_black.png")

        img = pygame.transform.scale(img, (60, 64))
        self.img = img

    def canMove(self, removed_figure, new_pos_x, new_pos_y):

        # Move only 1 place any direction
        if 0 <= new_pos_x <= 7 and self.pos_x - 1 <= new_pos_x <= self.pos_x + 1:
            if 0 <= new_pos_y <= 7 and self.pos_y - 1 <= new_pos_y <= self.pos_y + 1:

                # If opnt is King
                if isinstance(removed_figure, King):
                    return False
                return True

        else:
            return False
