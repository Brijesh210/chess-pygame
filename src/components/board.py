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
import json


class Board:
    color = None
    selected_figure = None
    removed_figure = None

    def __init__(self):
        self.figures = []
        self.board_pos = [[None for y in range(8)] for x in range(8)]
        self.next_turn = False

        with open("resources\\initial_position.json", "r") as file:
            self.piece_position = json.load(file)

        # source_square = "E2"
        # destination_square = "E4"
        # self.piece_position[destination_square] = self.piece_position[source_square]
        # del self.piece_position[source_square]

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

    def moveFigure(self, pos_x, pos_y):
        for figure in self.figures:
            if figure.pos_x == pos_x and figure.pos_y == pos_y:
                self.removed_figure = figure

        if self.selected_figure is not None and self.selected_figure.canMove(
            self.removed_figure, pos_x, pos_y, self.board_pos
        ):
            if self.removed_figure is None:
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

    def draw_board_pieces(self, screen):
        board_pieces = []
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    board_pieces.append(BoardPiece(i, j, COLOR_WHITE))
                else:
                    board_pieces.append(BoardPiece(i, j, COLOR_GRAY))

        for piece in board_pieces:
            piece.draw(screen)

    def draw_figures(self, screen):
        for figure in self.figures:
            if figure.isRemove == False:
                figure.draw(screen)

    def reset(self):
        self.figures.clear()
        color = None

        for square, piece in self.piece_position.items():
            col = 8 - int(square[1])
            row = ord(square[0].upper()) - ord("A")

            if piece[0] == "B":
                color = "Black"
            elif piece[0] == "W":
                color = "White"

            if piece[1] == "Q":
                self.figures.append(Queen(color, row, col))
            elif piece[1] == "K":
                self.figures.append(King(color, row, col))
            elif piece[1] == "N":
                self.figures.append(Knight(color, row, col))
            elif piece[1] == "P":
                self.figures.append(Pawn(color, row, col))
            elif piece[1] == "B":
                self.figures.append(Bishop(color, row, col))
            elif piece[1] == "R":
                self.figures.append(Rook(color, row, col))

        for figure in self.figures:
            self.board_pos[figure.pos_x][figure.pos_y] = figure


    def update_piece_position(self, pos_x, pos_y, new_piece):
        square = chr(ord("A") + pos_y) + str(pos_x + 1)
        self.piece_position[square] = new_piece
