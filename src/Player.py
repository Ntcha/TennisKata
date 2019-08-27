class Player:

    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __repr__(self):
        return f'{self.name}:{self.score}'
