import pygame as pg
from src.piece.pawn import Pawn
from src.piece.king import King 
from src.piece.queen import Queen  
from src.piece.rock import Rock 
from src.piece.knight import Knight
from src.piece.bishop import Bishop 
 



COLOR_GRAY = (128, 128, 128)
COLOR_WHITE = (255, 255, 255)


class BoardPiece():
    
    def __init__(self, pos_x , pos_y, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        
    def draw(self, screen):
        print(self.color)
        pg.draw.rect(screen, self.color, (self.pos_x * 64, self.pos_y * 64, 64, 64))



        
        
class Board():
    
    def __init__(self) -> None:
        self.figures = [Pawn(COLOR_WHITE, 1, 1), King(COLOR_WHITE, 4, 7)]
        
        self.boardPieces = []
        for i in range(8):
            for j in range(8):
                if (i + j) %2 == 0:
                    self.boardPieces.append(BoardPiece(i, j, COLOR_GRAY))
                else:
                    self.boardPieces.append(BoardPiece(i, j, COLOR_WHITE))   
        
    
    def selectFigure(x,y):
        # if can be selected then select else return
        pass
    
    def moveFigure(x,y):
        # if selected and if selected figure can move to target board piece then move it 
        # figures[selected.x,selected.y].move(x,y) 
        pass
                    
           
        
    def draw(self, screen):
        for piece in self.boardPieces:
            piece.draw(screen)
        
        for figure in self.figures: 
            figure.draw(screen)
        


        
            
   
        
    
        