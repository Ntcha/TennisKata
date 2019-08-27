class Score:

    def __init__(self):
        self.scale = ['Love', 'Fifteen', 'Thirty', 'Forty']
        self.deuce = 'Deuce'

    def announce(self, score_1, score_2):
        if score_1 < 0 or score_2 < 0 or score_1 > 3 or score_2 > 3:
            raise ValueError("Score values should be between 0 and 3 included")
        if score_1 == score_2 and score_1 == 3:
            return self.deuce;
        return f'{self.scale[score_1]} - {self.scale[score_2]}'
