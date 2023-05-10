import pygame
from . import board


class Figure:
    img = None
    isSelect: bool = False
    isRemove: bool = False

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def draw(self, screen):
        screen.blit(self.img, (self.pos_x * 64, 25 + self.pos_y * 64))
