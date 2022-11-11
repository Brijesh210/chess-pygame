import pygame as pg
from src.piece.pawn import Pawn
from src.piece.king import King 
from src.piece.queen import Queen  
from src.piece.rook import Rook 
from src.piece.knight import Knight
from src.piece.bishop import Bishop 
from src.figure import Figure
 



COLOR_GRAY = (128, 128, 200)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)



class BoardPiece():
    
    def __init__(self, pos_x , pos_y, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        
    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.pos_x * 64, self.pos_y * 64, 64, 64))



        
        
class Board():
    color = None
    selected_figure = None 
    removed_figure = None
    def __init__(self):
        self.figures = []
        self.boardPieces = []
        for i in range(8):
            for j in range(8):
                if (i + j) %2 == 0:
                    self.boardPieces.append(BoardPiece(i, j, COLOR_GRAY))
                else:
                    self.boardPieces.append(BoardPiece(i, j, COLOR_WHITE))   
        
    
    def selectFigure(self, pos_x, pos_y):
        for figure in self.figures: 
            if figure.pos_x == pos_x and figure.pos_y == pos_y:
                print("selected")
                self.selected_figure = figure
                self.selected_figure.isSelect = True
                self.color = figure.color
                    
        # if can be selected then select else return
        
    
    def moveFigure(self, pos_x, pos_y):
        # if selected and if selected figure can move to target board piece then move it 
        # figures[selected.x,selected.y].move(x,y) 
        # for figure in self.figures:
        #     if figure.isSelect == True:
        #         break 
        #     elif figure.pos_x == pos_x and figure.pos_y == pos_y:
        #         print("Deselected")
        #         figure.isRemove = True

        # for figure in self.figures:
        #     if figure.isSelect == True:
        #         figure.canMove(pos_x, pos_y)
        #         figure.isSelect = False
        for figure in self.figures: 
            if figure.pos_x == pos_x and figure.pos_y == pos_y:
                self.removed_figure = figure
        
        
        if self.selected_figure is not None:
            if self.selected_figure.canMove(pos_x, pos_y):
                if self.removed_figure == None:
                    self.selected_figure.pos_x = pos_x
                    self.selected_figure.pos_y = pos_y
                    self.selected_figure.isSelect  = False
                    self.selected_figure = None
                    self.color = None 
                
                if self.removed_figure is not None:
                    if self.removed_figure.color != self.color:
                        self.figures.remove(self.removed_figure)
                        self.removed_figure = None
                        self.selected_figure.pos_x = pos_x
                        self.selected_figure.pos_y = pos_y
                        self.selected_figure.isSelect  = False 
                        self.selected_figure = None
                        self.color = None
            else:
                self.selected_figure = None
                self.removed_figure = None
        else:
            self.selected_figure = None
            self.removed_figure = None
      
            # for figureR in self.figures:
            #     if figureR.pos_x == pos_x and figureR.pos_y == pos_y and figureR.color != self.color:        
            #         print("figure remove and placed new")
            #         self.figures.remove(figureR)
                    
            #         figure.pos_x = pos_x
            #         figure.pos_y = pos_y
            #         figure.isSelect = False
                    
            #     if figureR.pos_x == pos_x and figureR.pos_y == pos_y and figureR.color == self.color:
            #         print("No action taken")
            
            #     elif figure.pos_x != pos_x and figure.pos_y != pos_y:
            #         print("No image still move")
            #         figure.pos_x = pos_x
            #         figure.pos_y = pos_y
            #         figure.isSelect = False
                                    
           
        
    def draw_boardPieces(self, screen):
        for piece in self.boardPieces:
            piece.draw(screen)
    
    
    def draw_figures(self, screen):
        
        for figure in self.figures: 
            if figure.isRemove == False:
                figure.draw(screen)
        
        
    def reset(self):
        
        for i in range(8):
            self.figures.append(Pawn(COLOR_BLACK, i ,1))
            self.figures.append(Pawn(COLOR_WHITE, i, 6))
            
            
        # King
        
        self.figures.append(King(COLOR_BLACK, 4, 0))
        self.figures.append(King(COLOR_WHITE, 4, 7))
        
        # Queen
        self.figures.append(Queen(COLOR_BLACK, 3, 0))
        self.figures.append(Queen(COLOR_WHITE, 3, 7))
        
        # Bishop
        self.figures.append(Bishop(COLOR_BLACK, 2, 0))
        self.figures.append(Bishop(COLOR_BLACK, 5, 0))
        self.figures.append(Bishop(COLOR_WHITE, 2, 7))
        self.figures.append(Bishop(COLOR_WHITE, 5, 7))
        
        # Knight
        self.figures.append(Knight(COLOR_BLACK, 1, 0))
        self.figures.append(Knight(COLOR_BLACK, 6, 0))
        self.figures.append(Knight(COLOR_WHITE, 1, 7))
        self.figures.append(Knight(COLOR_WHITE, 6, 7))
        
        # Rook
        self.figures.append(Rook(COLOR_BLACK, 0, 0))
        self.figures.append(Rook(COLOR_BLACK, 7, 0))
        self.figures.append(Rook(COLOR_WHITE, 0, 7))
        self.figures.append(Rook(COLOR_WHITE, 7, 7))
        
        
    

        
            
   
        
    
        