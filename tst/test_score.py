import pytest

from src.Score import Score
from src.Game import Player


class Test_Score:

    @pytest.fixture
    def score(self):
        return Score()

    @pytest.fixture
    def player_1(self):
        return Player('Fab', 0)

    @pytest.fixture
    def player_2(self):
        return Player('Baf', 0)

    def test_score_has_score_scale(self, score):
        assert(score.scale)
        assert(len(score.scale) > 0)

    def test_score_knows_standard_tennis_scores(self, score):
        assert(score.scale[0] == 'Love')
        assert(score.scale[1] == 'Fifteen')
        assert(score.scale[2] == 'Thirty')
        assert(score.scale[3] == 'Forty')

    @pytest.mark.parametrize("score, player_1, player_2, expected", [
        (Score(), Player('Fab', 0), Player('Baf', 0), 'Fab : Love - Baf : Love'),
        (Score(), Player('Fab', 0), Player('Baf', 1), 'Fab : Love - Baf : Fifteen'),
        (Score(), Player('Fab', 0), Player('Baf', 2), 'Fab : Love - Baf : Thirty'),
        (Score(), Player('Fab', 0), Player('Baf', 3), 'Fab : Love - Baf : Forty'),
        (Score(), Player('Fab', 1), Player('Baf', 0), 'Fab : Fifteen - Baf : Love'),
        (Score(), Player('Fab', 2), Player('Baf', 0), 'Fab : Thirty - Baf : Love'),
        (Score(), Player('Fab', 3), Player('Baf', 0), 'Fab : Forty - Baf : Love'),
        (Score(), Player('Fab', 3), Player('Baf', 3), 'Deuce'),
        (Score(), Player('Fab', 5), Player('Baf', 5), 'Deuce'),
        (Score(), Player('Fab', 5), Player('Baf', 4), 'Fab, advantage'),
        (Score(), Player('Fab', 5), Player('Baf', 6), 'Baf, advantage')
    ])
    def test_score_can_announce(self, score, player_1, player_2, expected):
        assert(score.announce(player_1, player_2) == expected)

    @pytest.mark.parametrize("score, player_1, player_2, expected", [
        (Score(), Player('Fab', 0), Player('Baf', 0), False),
        (Score(), Player('Fab', 3), Player('Baf', 0), True),
        (Score(), Player('Fab', 3), Player('Baf', 3), False),
        (Score(), Player('Fab', 0), Player('Baf', 3), True),
        (Score(), Player('Fab', 5), Player('Baf', 3), True),
        (Score(), Player('Fab', 3), Player('Baf', 5), True),
    ])
    def test_game_over(self, score, player_1, player_2, expected):
        assert(score.is_game_over(player_1, player_2) == expected)
