from ..figure import Figure
import pygame


class Rook(Figure):
    def __init__(self, color, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.color = color

        if color == "White":
            img = pygame.image.load("resources\\rook_white.png")
        elif color == "Black":
            img = pygame.image.load("resources\\rook_black.png")

        img = pygame.transform.scale(img, (60, 64))
        self.img = img

    def canMove(self, removed_figure, new_pos_x, new_pos_y, boad_pos):
        if self.pos_x == new_pos_x:
            current_step = new_pos_y if self.pos_y > new_pos_y else self.pos_y
            max_step = self.pos_y if self.pos_y > new_pos_y else new_pos_y

            while current_step + 1 < max_step:
                if boad_pos[self.pos_x][current_step + 1] is not None:
                    return False

                current_step = current_step + 1
                
            return True

        elif self.pos_y == new_pos_y:
            current_step = new_pos_x if self.pos_x > new_pos_x else self.pos_x
            max_step = self.pos_x if self.pos_x > new_pos_x else new_pos_x

            while current_step + 1 < max_step:
                if boad_pos[current_step + 1][new_pos_y] is not None:
                    return False
                
                current_step = current_step + 1
                
            return True
        
        return False

