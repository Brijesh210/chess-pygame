import pygame
from src import board 
import math


BOARD_SIZZE_Y = 25
SIZE_X = 512
SIZE_Y = 512 + BOARD_SIZZE_Y

def main():
    font = 'Comic Sans MS'
    pygame.init()
    
    screen = pygame.display.set_mode((SIZE_X, SIZE_Y))
    screen.fill((200, 200, 200))
    pygame.display.set_caption("chess")
    pygame.font.init()
    font = pygame.font.SysFont(font, 30)
    running = True
 
 
    chess_board = board.Board(screen)
    chess_board.reset()
    chess_board.draw_boardPieces(screen)
    chess_board.draw_figures(screen)
    
    reset_button =  board.Button(screen, 448,0, "Reset")
    board.TextBox(screen, "Black turn")
    
    while running:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos() 
                chess_board.selectFigure(math.floor(pos[0] / 64), math.floor((pos[1] - BOARD_SIZZE_Y) / 64 ))
                if reset_button.rect.collidepoint(pos):
                    chess_board.reset()
             
                
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                chess_board.moveFigure(math.floor(pos[0] / 64), math.floor((pos[1] - BOARD_SIZZE_Y)/ 64 ))
                chess_board.draw_boardPieces(screen)
                chess_board.draw_figures(screen)
            
        
        pygame.display.update()


if __name__ == "__main__":
    main()