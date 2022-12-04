from enum import Enum


class StratRPS(Enum):
    LOSE = 0
    DRAW = 1
    WIN = 2


class RPS(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    @staticmethod
    def from_str_play(char: str):
        if char in ('A', 'X'):
            return RPS.ROCK
        elif char in ('B', 'Y'):
            return RPS.PAPER
        else:
            return RPS.SCISSORS

    @staticmethod
    def from_strat(rps_value, char):
        rps_start_matrix = [
            [RPS.SCISSORS, RPS.ROCK, RPS.PAPER],
            [RPS.ROCK, RPS.PAPER, RPS.SCISSORS],
            [RPS.PAPER, RPS.SCISSORS, RPS.ROCK]
        ]

        if char == 'X':
            return rps_start_matrix[rps_value][StratRPS.LOSE.value]
        elif char == 'Y':
            return rps_start_matrix[rps_value][StratRPS.DRAW.value]
        else:
            return rps_start_matrix[rps_value][StratRPS.WIN.value]
