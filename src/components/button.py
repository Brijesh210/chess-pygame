import pygame
from constants import COLOR_PURPLE, BUTTON_FONT


class Button:
    def __init__(self, screen, pos_x, pos_y, text, size_x, size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.text = text

        font = pygame.font.Font(BUTTON_FONT, 20)
        self.text = font.render(text, True, (0, 0, 0))

        self.text_rect = self.text.get_rect(
            center=(pos_x + size_x / 2, pos_y + size_y / 2)
        )
        self.screen = screen

    def draw(self):
        self.rect = pygame.draw.rect(
            self.screen,
            COLOR_PURPLE,
            (self.pos_x, self.pos_y, self.size_x, self.size_y),
        )
        self.screen.blit(self.text, self.text_rect)
