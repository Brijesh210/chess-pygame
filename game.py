import pygame
from src.components.board import Board
from src.components.text_box import TextBox
from src.components.button import Button
from src.components.player import Player

import math
from constants import BOARD_SIZZE_Y, SIZE_X, SIZE_Y, FONT, COLOR_LIGHT_GRAY
from network import Network


class Game:
    def __init__(self):
        pygame.init()
        Network()

        self.screen = pygame.display.set_mode((SIZE_X, SIZE_Y))
        self.screen.fill(COLOR_LIGHT_GRAY)

        pygame.display.set_caption("Chess")
        pygame.font.init()
        pygame.font.SysFont(FONT, 30)

        self.running = True
        self.game_started = False

        self.chess_board = Board(self.screen)
        self.chess_board.reset()
        self.chess_board.draw_boardPieces(self.screen)
        self.chess_board.draw_figures(self.screen)

        TextBox(self.screen, "white turn")

        self.reset_button = Button(self.screen, 448, 0, "Reset", 64, 24)
        self.quit_button = Button(self.screen, 383, 0, "Quit", 64, 24)
        self.start_button = Button(self.screen, 200, 250, "Start Game", 128, 64)
        
        """Player, Multiplayer network"""
        self.player_black = Player("Black")
        self.player_white = Player("White")
        
        
    def init_player(self):
        self.player_white.turn = True
        

    def handle_start_game_event(self):

        self.chess_board.reset()
        self.game_started = True

    def handle_reset_game_event(self):

        self.chess_board.reset()
        self.game_started = False

    def handle_mouse_button_down_event(self, pos):
        if self.game_started:
            self.chess_board.selectFigure(
                math.floor(pos[0] / 64),
                math.floor((pos[1] - BOARD_SIZZE_Y) / 64),
            )
            if self.reset_button.rect.collidepoint(pos):
                self.handle_reset_game_event()
        else:
            if self.start_button.rect.collidepoint(pos):
                self.handle_start_game_event()

    def handle_mouse_button_up_event(self, pos):
        if self.game_started:
            self.chess_board.moveFigure(
                math.floor(pos[0] / 64),
                math.floor((pos[1] - BOARD_SIZZE_Y) / 64),
            )
            self.chess_board.draw_boardPieces(self.screen)
            self.chess_board.draw_figures(self.screen)

    def play(self):

        while self.running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

                event_handlers = {
                    pygame.MOUSEBUTTONDOWN: self.handle_mouse_button_down_event,
                    pygame.MOUSEBUTTONUP: self.handle_mouse_button_up_event,
                }
                handler = event_handlers.get(event.type)

                if handler:
                    handler(pygame.mouse.get_pos())


                if not self.game_started:
                    self.start_button.draw()
                else:
                    self.reset_button.draw()


                pygame.display.update()
