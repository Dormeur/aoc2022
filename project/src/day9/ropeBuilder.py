from day9.coord import Coord
from day9.rope import Rope
from utils import read_file

file = read_file('../resources/input_day_9.txt')


def to_move(direction: str):
    match direction:
        case 'R':
            return Coord(1, 0)
        case 'L':
            return Coord(-1, 0)
        case 'U':
            return Coord(0, 1)
        case 'D':
            return Coord(0, -1)


def build_rope(tail_size):
    rope = Rope(tail_size)
    for direction, step in map(lambda line: line.split(), file):
        for _ in range(int(step)):
            rope.move(to_move(direction))

    print(rope.visited_positions.__len__())
