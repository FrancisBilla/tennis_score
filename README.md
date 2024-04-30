# tennis_score

Tennis has a rather quirky scoring system, and to newcomers it can be a little difficult to keep track of. Your
task is to build a Python program that displays the current score during a tennis game. The program should
accept input from an external input source (user input, file, etc.) and then display the current tennis score.
The program should keep accepting new scores until the user terminates the program.



1. Points are counted as 15, 30, 40, and then the game. So, a player starts at 0 (called "love"), then earns 15 points, followed by 30, then 40. If both players or teams are tied at 40, it's called "deuce."

2. After deuce, a player must win two consecutive points to win the game. If one player wins a point after deuce, it's called "advantage" for that player.

3. If the player with advantage wins the next point, they win the game. If they lose the next point, it goes back to deuce.

4. A set is won by the first player or team to win six games, with a margin of at least two games. If the score reaches 6-6, a tiebreaker is usually played.

5. In a tiebreaker, the first player or team to reach seven points wins, again with a margin of at least two points.

6. A match is usually the best of three sets, or in major tournaments, the best of five sets.