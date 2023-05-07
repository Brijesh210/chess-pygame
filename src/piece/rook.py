from ..figure import Figure  
import pygame

class Rook(Figure):
    
    def __init__(self, color, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.color = color
        
        if color == (255, 255, 255):
            img = pygame.image.load('res\\rook_white.png')
        elif color == (0,0,0):
            img = pygame.image.load('res\\rook_black.png')
            
        img = pygame.transform.scale(img, (60, 64))
        self.img = img
    
    def canMove(self, removed_figure, new_pos_x, new_pos_y, figures):
        if 0 <= new_pos_x <= 7 and new_pos_y == self.pos_y:
            z = abs(new_pos_x - self.pos_x)
            if removed_figure is not None:
                if removed_figure.pos_x in range(z-1):
                    return False
            else:
                return True

            
        elif 0 <= new_pos_y <= 7 and new_pos_x == self.pos_x:
            return True

        else:
            return False

    