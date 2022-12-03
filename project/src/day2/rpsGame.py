rps_score_matrix = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3]
]


class Game:
    def __init__(self, opponent_play, my_play):
        self.opponent_play = opponent_play
        self.my_play = my_play

    def get_score(self):
        return (self.my_play.value + 1) + self.compare_play()

    def compare_play(self):
        return rps_score_matrix[self.opponent_play.value][self.my_play.value]
