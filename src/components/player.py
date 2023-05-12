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
    
    def change_turn(self, first_player, second_player):
        
        if first_player.get_turn == True:
            first_player.get_turn = False
            second_player.get_turn = True 
        else:
            print("take your turn")
