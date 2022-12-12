class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def as_tuple(self) -> tuple:
        return self.x, self.y
