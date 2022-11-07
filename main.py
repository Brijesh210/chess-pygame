import pygame
from src import board 
import math

SIZE_X = 512
SIZE_Y = 512

def main():
    font = 'Comic Sans MS'
    pygame.init()
    
    screen = pygame.display.set_mode((SIZE_X, SIZE_Y))
    pygame.display.set_caption("chess")
    pygame.font.init()
    font = pygame.font.SysFont(font, 30)
    running = True
    
    color = (255, 0, 0)
    gray_color = (128, 128, 128)
    white_color = (255, 255, 255)
    
    inc = 64
 
 
 
    chess_board = board.Board()
    chess_board.draw(screen)
    
    # pawn1 = Pawn(white_color, 1, 1)
    # pawn1.draw(screen)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                # pawn1.move( math.floor(pos[0] / 64), math.floor(pos[1] / 64))
                # chess_board.draw(screen)
                # pawn1.draw(screen)
                pass
            if event.type == pygame.MOUSEBUTTONUP:
                # pos = pygame.mouse.get_pos()
                # print(pos)
                # pawn1.move( math.floor(pos[0] / 64), math.floor(pos[1] / 64))
                # chess_board.draw(screen)
                # pawn1.draw(screen)
                pass
        
        
        pygame.display.update()


if __name__ == "__main__":
    main()