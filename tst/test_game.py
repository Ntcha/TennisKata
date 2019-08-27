from src.Game import Game

class Test_Game:

    def test_game_has_2_players(self):
        game = Game(None, None)

        assert(len(game.players) == 2)

    def test_game_retains_user_names(self):
        player_1 = 'Fab'
        player_2 = 'Baf'

        game = Game(player_1, player_2)

        assert(game.players[0] == player_1)
        assert (game.players[1] == player_2)
