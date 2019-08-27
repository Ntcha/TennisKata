import pytest

from src.Score import Score


class Test_Score:

    @pytest.fixture
    def score(self):
        return Score()

    def test_score_has_score_scale(self, score):
        assert(score.scale)
        assert(len(score.scale) > 0)

    def test_score_knows_standard_tennis_scores(self, score):
        assert(score.scale[0] == 'Love')
        assert (score.scale[1] == 'Fifteen')
        assert (score.scale[2] == 'Thirty')
        assert (score.scale[3] == 'Forty')

    def test_score_can_announce(self, score):
        assert(score.announce(0, 0) == 'Love - Love')
        assert (score.announce(0, 3) == 'Love - Forty')
        assert (score.announce(1, 3) == 'Fifteen - Forty')
        assert (score.announce(2, 3) == 'Thirty - Forty')
