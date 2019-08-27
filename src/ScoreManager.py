class ScoreManager:

    def __init__(self):
        self.scale = ['Love', 'Fifteen', 'Thirty', 'Forty']
        self.deuce = 'Deuce'
        self.min_value_to_win = 3
        self.min_delta_to_win = 2

    def _order_players_by_score(self, player_1, player_2):
        if player_1.score > player_2.score:
            return player_1, player_2
        return player_2, player_1

    def _check_scores(self, score_1, score_2):
        if score_1 < 0 or score_2 < 0:
            raise ValueError("Score values should be greater than 0")

    def announce(self, player_1, player_2):
        self._check_scores(player_1.score, player_2.score)

        winner, looser = self._order_players_by_score(player_1, player_2)

        if winner.score == looser.score and \
                winner.score >= self.min_value_to_win:
            return self.deuce

        if winner.score > looser.score \
                and winner.score > self.min_value_to_win:
            return f'{winner.name}, advantage'

        return f'{player_1.name} : {self.scale[player_1.score]} -' \
               f' {player_2.name} : {self.scale[player_2.score]}'

    def is_game_over(self, player_1, player_2):
        self._check_scores(player_1.score, player_2.score)

        winner, looser = self._order_players_by_score(player_1, player_2)

        if winner.score >= self.min_value_to_win:
            if looser.score < self.min_value_to_win:
                return True
            if winner.score >= (looser.score + self.min_delta_to_win):
                return True

        return False

    def announce_winner(self, player_1, player_2):
        if not self.is_game_over(player_1, player_2):
            raise ValueError("Game is not over yet, continue to play !")

        winner, looser = self._order_players_by_score(player_1, player_2)
        return f'{winner.name} is the winner'
