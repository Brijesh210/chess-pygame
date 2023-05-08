from src.player import Player


def test_get_id():
    player = Player(2, True)
    piece_colour = player.get_piece_colour()
    assert piece_colour == 2
