class Score:

    def __init__(self):
        self.scale = ['Love', 'Fifteen', 'Thirty', 'Forty']

    def announce(self, score_1, score_2):
        if score_1 < 0 or score_2 < 0 or score_1 > 3 or score_2 > 3:
            raise ValueError("Score values should be between 0 and 3 included")
        return f'{self.scale[score_1]} - {self.scale[score_2]}'
