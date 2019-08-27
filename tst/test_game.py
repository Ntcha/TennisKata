import pytest
from src.Game import Game
from src.Player import Player
from src.ScoreManager import ScoreManager


class Test_Game:

    def test_game_has_2_players(self):
        game = Game(None, None, None)

        assert(len(game.players) == 2)

    def test_game_retains_user_names(self,):
        game = Game('Fab', 'Baf', None)

        assert(game.players[0].name == 'Fab')
        assert (game.players[1].name == 'Baf')

    def test_game_player_have_scores(self):
        game = Game('Fab', 'Baf', None)

        assert(game.players[0].score == 0)
        assert (game.players[1].score == 0)

    @pytest.mark.parametrize('player_1, player_2, score_manager, expected', [
        (Player('Fab', 4), Player('Baf', 0), ScoreManager(), True),
        (Player('Fab', 5), Player('Baf', 3), ScoreManager(), True),
        (Player('Fab', 5), Player('Baf', 4), ScoreManager(), False)
    ])
    def test_game_is_over(self, player_1, player_2, score_manager, expected):
        game = Game(None, None, score_manager)

        game.players[0].name = player_1.name
        game.players[0].score = player_1.score
        game.players[1].name = player_2.name
        game.players[1].score = player_2.score

        assert(game.is_over() == expected)

    @pytest.mark.parametrize('player_number, players, score_manager, expected',
    [
        (1, [Player('Fab', 0), Player('Baf', 0)], ScoreManager(), 1),
        (2, [Player('Fab', 2), Player('Baf', 3)], ScoreManager(), 4),
        (1, [Player('Fab', 2), Player('Baf', 3)], ScoreManager(), 3),
    ])
    def test_player_marks(self, player_number, players, score_manager,
                           expected):
        game = Game(None, None, score_manager)

        game.players[0] = players[0]
        game.players[1] = players[1]

        entry_score = players[player_number - 1].score

        game.player_marks(player_number)
        assert(players[player_number - 1].score == entry_score + 1)
