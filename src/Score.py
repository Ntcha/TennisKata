class Score:

    def __init__(self):
        self.scale = ['Love', 'Fifteen', 'Thirty', 'Forty']
        self.deuce = 'Deuce'

    def announce(self, player_1_name, score_1, player_2_name, score_2):
        if score_1 < 0 or score_2 < 0:
            raise ValueError("Score values should be greater than 0")

        if score_1 == score_2 and score_1 >= 3:
            return self.deuce

        if score_1 > score_2 and score_1 > 3:
            return f'{player_1_name}, advantage'

        if score_2 > score_1 and score_2 > 3:
            return f'{player_2_name}, advantage'

        return f'{self.scale[score_1]} - {self.scale[score_2]}'

    def is_game_over(self,score_1, score_2):
        highest_score, lowest_score = score_1 > score_2 and (score_1, score_2) or (score_2, score_1)

        if highest_score >= 3 and highest_score >= lowest_score + 2:
            return True

        return False
