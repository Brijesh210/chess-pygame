import pygame


class BoardPiece:
    def __init__(self, pos_x, pos_y, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(
            screen, self.color, (self.pos_x * 64, 25 + self.pos_y * 64, 64, 64)
        )
