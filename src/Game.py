from collections import namedtuple

Player = namedtuple('Player', ['name', 'score'])


class Game:

    def __init__(self, first_player_name, second_player_name):
        self.players = [Player(first_player_name, 0),
                        Player(second_player_name, 0)]
