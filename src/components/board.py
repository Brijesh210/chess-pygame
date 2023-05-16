from .piece.pawn import Pawn
from .piece.king import King
from .piece.queen import Queen
from .piece.rook import Rook
from .piece.knight import Knight
from .piece.bishop import Bishop
from .figure import Figure
from constants import COLOR_GRAY, COLOR_WHITE, COLOR_BLACK
from .board_piece import BoardPiece
from .player import Player


class Board:
    color = None
    selected_figure = None
    removed_figure = None

    def __init__(self, screen):
        self.figures = []
        self.boardPieces = []
        self.board_pos = [[None for y in range(8)] for x in range(8)]
        self.next_turn = False

        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    self.boardPieces.append(BoardPiece(i, j, COLOR_GRAY))
                else:
                    self.boardPieces.append(BoardPiece(i, j, COLOR_WHITE))

    def selectFigure(self, pos_x, pos_y, colour):
        selected_figure = next(
            (
                figure
                for figure in self.figures
                if figure.pos_x == pos_x
                and figure.pos_y == pos_y
                and figure.color == colour
            ),
            None,
        )

        if selected_figure is not None:
            print("selected")
            self.selected_figure = selected_figure
            self.color = self.selected_figure.color
            print(self.color)

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
                    self.next_turn = True

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
                        self.next_turn = True

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
            self.figures.append(Pawn("Black", i, 1))
            self.figures.append(Pawn("White", i, 6))

        # King

        self.figures.append(King("Black", 4, 0))
        self.figures.append(King("White", 4, 7))

        # Queen
        self.figures.append(Queen("Black", 3, 0))
        self.figures.append(Queen("White", 3, 7))

        # Bishop
        self.figures.append(Bishop("Black", 2, 0))
        self.figures.append(Bishop("Black", 5, 0))
        self.figures.append(Bishop("White", 2, 7))
        self.figures.append(Bishop("White", 5, 7))

        # Knight
        self.figures.append(Knight("Black", 1, 0))
        self.figures.append(Knight("Black", 6, 0))
        self.figures.append(Knight("White", 1, 7))
        self.figures.append(Knight("White", 6, 7))

        # Rook
        self.figures.append(Rook("Black", 0, 0))
        self.figures.append(Rook("Black", 7, 0))
        self.figures.append(Rook("White", 0, 7))
        self.figures.append(Rook("White", 7, 7))

        for figure in self.figures:
            self.board_pos[figure.pos_x][figure.pos_y] = figure

    def quit(self):
        return
