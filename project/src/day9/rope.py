from day9.coord import Coord


def signed_step(n):
    return 0 if n == 0 else 1 if n > 0 else -1


class Rope:
    def __init__(self, tail_size):
        self.tail_size = tail_size
        self.sections = [Coord(0, 0) for _ in range(tail_size)]
        self.head = Coord(0, 0)
        self.sections.insert(0, self.head)
        self.visited_positions = {(0, 0)}

    def move(self, move: Coord):
        self.head += move

        for i in range(self.tail_size):
            current_head = self.sections[i]
            dif_x = current_head.x - self.sections[i + 1].x
            dif_y = current_head.y - self.sections[i + 1].y

            if abs(dif_x) > 1 or abs(dif_y) > 1:
                self.sections[i + 1] += Coord(signed_step(dif_x), signed_step(dif_y))
                
        self.visited_positions.add(self.sections[-1].as_tuple())
