
import pytest
from tennis_score_system import TennisScoreCalculator


@pytest.fixture
def tennis_calculator():
    return TennisScoreCalculator()


def test_log_score(tennis_calculator):
    tennis_calculator.log_score(1)
    assert tennis_calculator.player1_score == 1

    tennis_calculator.log_score(2)
    assert tennis_calculator.player2_score == 1


def test_check_game_won(tennis_calculator):
    tennis_calculator.player1_score = 4
    tennis_calculator.player2_score = 2
    tennis_calculator.check_game_won()
    assert tennis_calculator.player1_games == 1

    tennis_calculator.player1_score = 3
    tennis_calculator.player2_score = 5
    tennis_calculator.check_game_won()
    assert tennis_calculator.player2_games == 1


def test_get_regular_score(tennis_calculator):
    tennis_calculator.player1_score = 3
    tennis_calculator.player2_score = 2
    assert tennis_calculator.get_regular_score() == "40-30"


def test_get_advantage_score(tennis_calculator):
    tennis_calculator.log_score(1)
    tennis_calculator.log_score(1)
    tennis_calculator.log_score(1)
    tennis_calculator.log_score(2)
    tennis_calculator.log_score(2)
    tennis_calculator.log_score(2)
    tennis_calculator.log_score(2)
    assert tennis_calculator.get_score() == "Advantage Player 2"
    tennis_calculator.log_score(1)
    tennis_calculator.log_score(1)
    assert tennis_calculator.get_score() == "Advantage Player 1"


def test_get_game_score(tennis_calculator):
    tennis_calculator.player1_score = 4
    tennis_calculator.player2_score = 2
    assert tennis_calculator.get_game_score() == "Game Player 1"


def test_game_won(tennis_calculator):
    tennis_calculator.log_score(1)
    tennis_calculator.log_score(1)
    tennis_calculator.log_score(1)
    tennis_calculator.log_score(1)
    tennis_calculator.log_score(1)
    assert tennis_calculator.player1_games == 1


def test_player1_wins_game(tennis_calculator):
    tennis_calculator.player1_score = 4
    tennis_calculator.player2_score = 2
    tennis_calculator.check_game_won()
    assert tennis_calculator.player1_games == 1
    assert tennis_calculator.player2_games == 0
    assert tennis_calculator.player1_score == 0
    assert tennis_calculator.player2_score == 0


def test_player2_wins_game(tennis_calculator):
    tennis_calculator.player1_score = 3
    tennis_calculator.player2_score = 5
    tennis_calculator.check_game_won()
    assert tennis_calculator.player1_games == 0
    assert tennis_calculator.player2_games == 1
    assert tennis_calculator.player1_score == 0
    assert tennis_calculator.player2_score == 0


def test_reset_scores(tennis_calculator):
    tennis_calculator.player1_score = 4
    tennis_calculator.player2_score = 2
    tennis_calculator.check_game_won()
    assert tennis_calculator.player1_score == 0
    assert tennis_calculator.player2_score == 0
