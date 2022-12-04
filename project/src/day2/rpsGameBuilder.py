from day2.rpsEnum import RPS
from day2.rpsGame import Game
from utils import read_file

games = []


def build_game_list():
    games.clear()
    f = read_file("../ressources/input_day_2.txt")
    for line in f:
        opponent_play = RPS.from_str_play(line[0])
        my_play = RPS.from_str_play(line[2])
        games.append(Game(opponent_play, my_play))


def build_game_with_strat_list():
    games.clear()
    f = read_file("../ressources/input_day_2.txt")
    for line in f:
        opponent_play = RPS.from_str_play(line[0])
        my_play = RPS.from_strat(opponent_play.value, line[2])
        games.append(Game(opponent_play, my_play))


def get_total_score():
    print(sum(game.get_score() for game in games))
