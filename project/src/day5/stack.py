from typing import List, Tuple

SPACE = ' '


def remove_space(itr: Tuple[str]) -> list:
    return list(filter(lambda s: not s.isspace(), itr))


class Move:
    def __init__(self, move: str):
        self.quantity, self.from_stack, self.end_stack = map(int, filter(lambda s: s.isnumeric(), move.split(SPACE)))
        self.from_stack -= 1
        self.end_stack -= 1


class Stack:
    def __init__(self, crates):
        self.crates: List[str] = remove_space(crates)
        self.crates.reverse()

    def get_top_crate(self) -> str:
        return self.crates[-1]
