class Player:
    def __init__(self, colour) -> None:
        self.colour = colour
        if self.colour == "White":
            self.turn = True
        elif self.colour == "Black":
            self.turn = False

    def get_colour(self):
        return self.colour

    def has_turn(self):
        return self.turn

    def change_turn(self):
        if self.colour == "White":
            self.colour = "Black"
        elif self.colour == "Black":
            self.colour = "White"
