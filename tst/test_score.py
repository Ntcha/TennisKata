import pytest

from src.Score import Score


class Test_Score:
    @pytest.fixture
    def score(self):
        return Score()

    def test_score_has_score_scale(self, score):
        assert(score.scale)
        assert(len(score.scale) > 0)
