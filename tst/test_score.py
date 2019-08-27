import pytest

from src.Score import Score


class Test_Score:

    @pytest.fixture
    def score(self):
        return Score()

    @pytest.fixture
    def player_1(self):
        return 'Fab'

    @pytest.fixture
    def player_2(self):
        return 'Baf'

    def test_score_has_score_scale(self, score):
        assert(score.scale)
        assert(len(score.scale) > 0)

    def test_score_knows_standard_tennis_scores(self, score):
        assert(score.scale[0] == 'Love')
        assert (score.scale[1] == 'Fifteen')
        assert (score.scale[2] == 'Thirty')
        assert (score.scale[3] == 'Forty')

    def test_score_can_announce(self, score, player_1, player_2):
        assert(score.announce(player_1, 0, player_2, 0) == 'Love - Love')
        assert(score.announce(player_1, 0, player_2, 3) == 'Love - Forty')
        assert(score.announce(player_1, 1, player_2, 3) == 'Fifteen - Forty')
        assert(score.announce(player_1, 2, player_2, 3) == 'Thirty - Forty')

    def test_score_can_announce_deuce(self, score, player_1, player_2):
        assert(score.announce(player_1, 3, player_2, 3) == 'Deuce')
        assert (score.announce(player_1, 5, player_2, 5) == 'Deuce')

    def test_score_can_announce_advantage(self, score, player_1, player_2):
        assert(score.announce(player_1, 4, player_2, 3,)
               == f'{player_1}, advantage')
        assert (score.announce(player_1, 7, player_2, 8, )
                == f'{player_2}, advantage')

    def test_game_over(self, score):
        assert(not score.is_game_over(0, 0))
        assert(score.is_game_over(0, 3))

    def test_game_over_advantage(self, score):
        assert (not score.is_game_over(3, 3))
        assert (not score.is_game_over(4, 3))
        assert (not score.is_game_over(4, 4))
        assert (score.is_game_over(4, 6))
        assert (score.is_game_over(8, 6))
