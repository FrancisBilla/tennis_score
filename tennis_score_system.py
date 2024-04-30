class TennisScoreCalculator:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
        self.player1_games = 0
        self.player2_games = 0
        self.current_game = 1

    def point_scored(self, player):
        if player == 1:
            self.player1_score += 1
        elif player == 2:
            self.player2_score += 1
        else:
            raise ValueError("Invalid player number")
        self.current_game += 1
        self.check_game_won()

    def check_game_won(self):
        if (abs(self.player1_score - self.player2_score) >= 2 and
                (self.player1_score >= 4 or self.player2_score >= 4)):
            if self.player1_score > self.player2_score:
                self.player1_games += 1
                print("Player 1 won the game!")
            else:
                self.player2_games += 1
                print("Player 2 won the game!")
            self.player1_score = 0
            self.player2_score = 0

    def get_score(self):
        if self.player1_score < 4 and self.player2_score < 4:
            return self.get_regular_score()
        elif self.player1_score >= 3 and self.player2_score >= 3:
            return self.get_advantage_score()
        else:
            return self.get_game_score()

    def get_regular_score(self):
        score_names = ["Love", "15", "30", "40"]
        score1 = score_names[self.player1_score]
        score2 = score_names[self.player2_score]

        if score1 and score2 == "40":
            return f"Deuce {score1}-{score2}"
        else:
            return f"{score1}-{score2}"

    def get_deuce_score(self):
        print("Deuce")

    def get_advantage_score(self):
        if self.player1_score == self.player2_score:
            self.get_deuce_score()

        diff = self.player1_score - self.player2_score
        if diff == 1:
            return "Advantage Player 1"
        elif diff == -1:
            return "Advantage Player 2"

    def get_game_score(self):
        diff = self.player1_score - self.player2_score
        if diff >= 2:
            return "Game Player 1"
        elif diff <= -2:
            return "Game Player 2"

    def check_set_won(self):
        if max(self.player1_games, self.player2_games) >= 6:
            if abs(self.player1_games - self.player2_games) >= 2:
                if self.player1_games > self.player2_games:
                    print("Player 1 won the set!")
                else:
                    print("Player 2 won the set!")
                self.current_set += 1
                self.reset_game()


def main():
    game = TennisScoreCalculator()

    # Accept input from the user until terminated
    while True:
        try:
            player = int(
                input("Enter player number who scored (1 or 2),"
                      " or enter '0' to exit: "))
            if player == 0:
                print("Exiting...")
                break
            elif player not in [1, 2]:
                print("Invalid player number. Please enter 1 or 2.")
                continue
            game.point_scored(player)
            print("Current score:", game.get_score())
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
