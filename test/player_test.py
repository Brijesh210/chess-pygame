from src.components.player import Player


def test_get_id():
    player = Player("White")
    piece_colour = player.get_colour()
    assert piece_colour == "White"
