import pytest

from src.Score import Score
from src.Game import Player


class Test_Score:

    @pytest.fixture
    def score(self):
        return Score()

    def test_score_has_score_scale(self, score):
        assert(score.scale)
        assert(len(score.scale) > 0)

    @pytest.mark.parametrize('score, value, expected', [
        (Score(), 0, 'Love'),
        (Score(), 1, 'Fifteen'),
        (Score(), 2, 'Thirty'),
        (Score(), 3, 'Forty')
    ])
    def test_score_knows_standard_tennis_scores(self, score, value, expected):
        assert(score.scale[value] == expected)

    @pytest.mark.parametrize('score, player_1, player_2, expected', [
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

    @pytest.mark.parametrize('score, player_1, player_2, expected', [
        (Score(), Player('Fab', 0), Player('Baf', 0), False),
        (Score(), Player('Fab', 3), Player('Baf', 0), True),
        (Score(), Player('Fab', 3), Player('Baf', 3), False),
        (Score(), Player('Fab', 0), Player('Baf', 3), True),
        (Score(), Player('Fab', 5), Player('Baf', 3), True),
        (Score(), Player('Fab', 3), Player('Baf', 5), True),
    ])
    def test_game_over(self, score, player_1, player_2, expected):
        assert(score.is_game_over(player_1, player_2) == expected)

    @pytest.mark.parametrize('score, player_1, player_2, expected', [
        (Score(), Player('Fab', 3), Player('Baf', 0), 'Fab is the winner'),
        (Score(), Player('Fab', 0), Player('Baf', 3), 'Baf is the winner'),
        (Score(), Player('Fab', 5), Player('Baf', 3), 'Fab is the winner'),
        (Score(), Player('Fab', 3), Player('Baf', 5), 'Baf is the winner'),
    ])
    def test_announce_winner(self, score, player_1, player_2, expected):
        assert(score.announce_winner(player_1, player_2) == expected)

    @pytest.mark.parametrize('score, player_1, player_2', [
        (Score(), Player('Fab', 2), Player('Baf', 0)),
        (Score(), Player('Fab', 3), Player('Baf', 3)),
        (Score(), Player('Fab', 5), Player('Baf', 4)),
        (Score(), Player('Fab', 4), Player('Baf', 5)),
    ])
    def test_announce_winner_exceptions(self, score, player_1, player_2):
        with pytest.raises(ValueError):
            assert(score.announce_winner(player_1, player_2))

