import pygame 


class TextBox:
    def __init__(self, screen, text):
        font = pygame.font.Font("freesansbold.ttf", 20)
        self.text = font.render(text, True, (0, 0, 0))
        screen.blit(self.text, (200, 3))


