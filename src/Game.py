from collections import namedtuple

Player = namedtuple('Player', ['name', 'score'])


class Game:

    def __init__(self, first_player_name, second_player_name, score_manager):
        self.players = [Player(first_player_name, 0),
                        Player(second_player_name, 0)]

        self.score_manager = score_manager

    def is_over(self):
        return self.score_manager.is_game_over(self.players[0], self.players[1])

