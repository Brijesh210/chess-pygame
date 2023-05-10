class Player:
    def __init__(self, piece_colour, turn=False) -> None:
        self.piece_colour = piece_colour
        self.turn = turn

    def get_piece_colour(self):
        return self.piece_colour

    def get_turn(self):
        return self.turn
