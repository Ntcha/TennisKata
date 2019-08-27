from src.Player import Player


class Game:

    def __init__(self, first_player_name, second_player_name, score_manager):
        self.players = [Player(first_player_name, 0),
                        Player(second_player_name, 0)]

        self.score_manager = score_manager

    def is_over(self):
        return self.score_manager.is_game_over(self.players[0],
                                               self.players[1])

    def player_marks(self, player_number):
        self.players[player_number - 1].score += 1
        if self.is_over():
            print(self.score_manager.announce_winner(self.players[0],
                                                     self.players[1]))
        else:
            print(self.score_manager.announce(self.players[0],
                                              self.players[1]))
