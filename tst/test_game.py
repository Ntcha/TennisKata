import pytest
from src.Game import Game, Player
from src.ScoreManager import ScoreManager

class Test_Game:

    @pytest.fixture
    def player_1(self):
        return 'Fab'

    @pytest.fixture
    def player_2(self):
        return 'baf'

    def test_game_has_2_players(self):
        game = Game(None, None, None)

        assert(len(game.players) == 2)

    def test_game_retains_user_names(self, player_1, player_2):
        game = Game(player_1, player_2, None)

        assert(game.players[0].name == player_1)
        assert (game.players[1].name == player_2)

    def test_game_player_have_scores(self, player_1, player_2):
        game = Game(player_1, player_2, None)

        assert(game.players[0].score == 0)
        assert (game.players[1].score == 0)

    @pytest.mark.parametrize('player_1, player_2, score_manager, expected', [
        (Player('Fab', 3), Player('Baf', 0), ScoreManager(), True),
        (Player('Fab', 5), Player('Baf', 3), ScoreManager(), True),
        (Player('Fab', 5), Player('Baf', 4), ScoreManager(), False)
    ])
    def test_game_is_over(self, player_1, player_2, score_manager, expected):
        game = Game(None, None, score_manager)

        game.players[0] = player_1
        game.players[1] = player_2

        assert(game.is_over() == expected)

            
