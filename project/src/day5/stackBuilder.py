from day5.stack import *
from utils import read_file

stacks: List[Stack]
moves: List[Move]


def remove_empty_column(itr):
    return filter(lambda col: col[-1].isnumeric(), itr)


def fill_row_with_space(itr):
    return map(lambda s: s.ljust(max(itr, key=len).__len__()), itr)


def format_stack_graph(stack_graph):
    return remove_empty_column(zip(*fill_row_with_space(stack_graph)))


def build_stack_and_move_list():
    global stacks, moves
    f = read_file('../resources/input_day_5.txt')
    empty_line_index = f.index('')
    stacks = list(map(Stack, format_stack_graph(f[:empty_line_index])))
    moves = list(map(Move, f[empty_line_index + 1:]))


def start_crate_mover_9000():
    for move in moves:
        stacks[move.end_stack].crates.extend([stacks[move.from_stack].crates.pop() for _ in range(move.quantity)])


def start_crate_mover_9001():
    for move in moves:
        stacks[move.end_stack].crates.extend(stacks[move.from_stack].crates[-move.quantity:])
        del stacks[move.from_stack].crates[-move.quantity:]


def get_all_top_crate():
    print(''.join(map(lambda stack: stack.get_top_crate(), stacks)))
