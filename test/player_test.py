from src.player import Plyer

def test_get_id():
    player = Plyer(2, True)
    id = player.get_id()
    assert id == 2