from ..figure import Figure  
import pygame

class Knight(Figure):
    
    def __init__(self, color, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        if color == (255, 255, 255):
            img = pygame.image.load('res\\knight_white.png')
        elif color == (0,0,0):
            img = pygame.image.load('res\\knight_black.png')
            
        img = pygame.transform.scale(img, (64, 64))
        self.img = img
    
    def canMove(new_pos_x, new_pos_y):
        if new_pos_x == 2:
            return True
        return False
    