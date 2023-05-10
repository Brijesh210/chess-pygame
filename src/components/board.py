import pygame as pg
from .piece.pawn import Pawn
from .piece.king import King
from .piece.queen import Queen
from .piece.rook import Rook
from .piece.knight import Knight
from .piece.bishop import Bishop
from .figure import Figure
from .player import Player
from constants import COLOR_GRAY, COLOR_WHITE, COLOR_BLACK



class TextBox:
    def __init__(self, screen, text):
        font = pg.font.Font("freesansbold.ttf", 20)
        self.text = font.render(text, True, (0, 0, 0))
        screen.blit(self.text, (200, 3))


class BoardPiece:
    def __init__(self, pos_x, pos_y, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color

    def draw(self, screen):
        pg.draw.rect(
            screen, self.color, (self.pos_x * 64, 25 + self.pos_y * 64, 64, 64)
        )


class Board:
    color = None
    selected_figure = None
    removed_figure = None

    def __init__(self, screen):
        self.figures = []
        self.boardPieces = []
        self.board_pos = [[None for y in range(8)] for x in range(8)]

        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    self.boardPieces.append(BoardPiece(i, j, COLOR_GRAY))
                else:
                    self.boardPieces.append(BoardPiece(i, j, COLOR_WHITE))

    def selectFigure(self, pos_x, pos_y):
        for figure in self.figures:
            if figure.pos_x == pos_x and figure.pos_y == pos_y:
                print("selected")
                self.selected_figure = figure
                self.color = figure.color

    def moveFigure(self, pos_x, pos_y):

        for figure in self.figures:
            if figure.pos_x == pos_x and figure.pos_y == pos_y:
                self.removed_figure = figure

        if self.selected_figure is not None:

            if self.selected_figure.canMove(
                self.removed_figure, pos_x, pos_y, self.board_pos
            ):
                if self.removed_figure == None:
                    self.board_pos[self.selected_figure.pos_x][
                        self.selected_figure.pos_y
                    ] = None
                    self.selected_figure.pos_x = pos_x
                    self.selected_figure.pos_y = pos_y
                    self.board_pos[self.selected_figure.pos_x][
                        self.selected_figure.pos_y
                    ] = self.selected_figure
                    self.selected_figure = None
                    self.color = None

                if self.removed_figure is not None:
                    if self.removed_figure.color != self.color:
                        self.figures.remove(self.removed_figure)
                        self.board_pos[self.removed_figure.pos_x][
                            self.removed_figure.pos_y
                        ] = None
                        self.removed_figure = None
                        self.board_pos[self.selected_figure.pos_x][
                            self.selected_figure.pos_y
                        ] = None
                        self.selected_figure.pos_x = pos_x
                        self.selected_figure.pos_y = pos_y
                        self.board_pos[self.selected_figure.pos_x][
                            self.selected_figure.pos_y
                        ] = self.selected_figure
                        self.selected_figure = None
                        self.color = None

            else:
                self.selected_figure = None
                self.removed_figure = None
        else:
            self.selected_figure = None
            self.removed_figure = None

    def draw_boardPieces(self, screen):
        for piece in self.boardPieces:
            piece.draw(screen)

    def draw_figures(self, screen):

        for figure in self.figures:
            if figure.isRemove == False:
                figure.draw(screen)

    def reset(self):
        self.figures.clear()

        for i in range(8):
            self.figures.append(Pawn(COLOR_BLACK, i, 1))
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

        for figure in self.figures:
            self.board_pos[figure.pos_x][figure.pos_y] = figure

    def start(self):
        player_black = Player("black")
        player_white = Player("white")

        player_white.turn = True

    def quit(self):
        return


