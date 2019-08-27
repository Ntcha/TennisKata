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

    @pytest.mark.parametrize("score, player_1_name, player_1_score, \
                             player_2_name, player_2_score, expected", [
        (Score(), 'Fab', 0, 'Baf', 0, 'Fab : Love - Baf : Love'),
        (Score(), 'Fab', 0, 'Baf', 1, 'Fab : Love - Baf : Fifteen'),
        (Score(), 'Fab', 0, 'Baf', 2, 'Fab : Love - Baf : Thirty'),
        (Score(), 'Fab', 0, 'Baf', 3, 'Fab : Love - Baf : Forty'),
        (Score(), 'Fab', 1, 'Baf', 0, 'Fab : Fifteen - Baf : Love'),
        (Score(), 'Fab', 2, 'Baf', 0, 'Fab : Thirty - Baf : Love'),
        (Score(), 'Fab', 3, 'Baf', 0, 'Fab : Forty - Baf : Love'),
        (Score(), 'Fab', 3, 'Baf', 3, 'Deuce'),
        (Score(), 'Fab', 4, 'Baf', 4, 'Deuce'),
        (Score(), 'Fab', 5, 'Baf', 4, 'Fab, advantage'),
        (Score(), 'Fab', 5, 'Baf', 6, 'Baf, advantage')
    ])
    def test_score_can_announce(self, score, player_1_name, player_1_score,
                                player_2_name, player_2_score, expected):
        player_1 = Player(player_1_name, player_1_score)
        player_2 = Player(player_2_name, player_2_score)
        assert(score.announce(player_1, player_2) == expected)

    def test_game_over(self, score):
        assert(not score.is_game_over(0, 0))
        assert(score.is_game_over(0, 3))

    def test_game_over_advantage(self, score):
        assert(not score.is_game_over(3, 3))
        assert(not score.is_game_over(4, 3))
        assert(not score.is_game_over(4, 4))
        assert(score.is_game_over(4, 6))
        assert(score.is_game_over(8, 6))
