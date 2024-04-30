import pytest
from tennis_score_system import TennisScoreCalculator


@pytest.fixture
def game():
    return TennisScoreCalculator()


def test_regular_score(game):
    game.point_scored(1)
    assert game.get_score() == "15-Love"
    game.point_scored(2)
    assert game.get_score() == "15-15"
    game.point_scored(2)
    assert game.get_score() == "15-30"
    game.point_scored(1)
    game.point_scored(1)
    assert game.get_score() == "40-30"
    game.point_scored(2)
    assert game.get_score() == "Deuce 40-40"


def test_advantage_score(game):
    game.point_scored(1)
    game.point_scored(1)
    game.point_scored(1)
    game.point_scored(2)
    game.point_scored(2)
    game.point_scored(2)
    game.point_scored(2)
    assert game.get_score() == "Advantage Player 2"
    game.point_scored(1)
    game.point_scored(1)
    assert game.get_score() == "Advantage Player 1"


def test_game_won(game):
    game.point_scored(1)
    game.point_scored(1)
    game.point_scored(1)
    game.point_scored(1)
    game.point_scored(1)
    assert game.player1_games == 1


def test_player1_wins_game(game):
    game.player1_score = 4
    game.player2_score = 2
    game.check_game_won()
    assert game.player1_games == 1
    assert game.player2_games == 0
    assert game.player1_score == 0
    assert game.player2_score == 0


def test_player2_wins_game(game):
    game.player1_score = 3
    game.player2_score = 5
    game.check_game_won()
    assert game.player1_games == 0
    assert game.player2_games == 1
    assert game.player1_score == 0
    assert game.player2_score == 0


def test_reset_scores(game):
    game.player1_score = 4
    game.player2_score = 2
    game.check_game_won()
    assert game.player1_score == 0
    assert game.player2_score == 0