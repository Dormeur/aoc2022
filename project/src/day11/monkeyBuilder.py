import operator
from functools import reduce

import numpy as np

from day11.monkey import Monkey
from day11.monkeyMapper import to_monkey
from utils import read_file

f = read_file('../resources/input_day_11.txt')


def build_monkey_list(number_of_rounds):
    monkeys: list[Monkey] = []

    for paragraph in np.array_split(f, 8):
        monkeys.append(to_monkey(paragraph))

    mod = reduce(operator.mul, [monkey.divisible_test for monkey in monkeys])

    for turn in range(number_of_rounds):
        for monkey in monkeys:
            monkey.play_turn(monkeys, mod)

    print(reduce(operator.mul, sorted(monkey.inspection for monkey in monkeys)[-2:]))
