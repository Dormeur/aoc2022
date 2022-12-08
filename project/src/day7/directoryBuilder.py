from typing import List

from utils import read_file

SYSTEM_SIZE = 70000000
UPDATE_SIZE = 30000000


class Directory:

    def __init__(self, parent):
        self.parent = parent
        self.dir: dict[str, Directory] = {}
        self.size: int = 0

    def get_full_size(self):
        return self.size + sum(d.get_full_size() for d in self.dir.values())


def build_directory():
    f = read_file('../resources/input_day_7.txt')
    current_dir = Directory('')
    system: List[Directory] = [current_dir]
    for line in filter(lambda l: l not in ['$ cd /', '$ ls'], f):
        if line.startswith('dir'):
            current_dir.dir[line[4:]] = Directory(current_dir)
            system.append(current_dir.dir.get(line[4:]))
        elif line.startswith('$ cd ..'):
            current_dir = current_dir.parent
        elif line.startswith('$ cd'):
            current_dir = current_dir.dir.get(line[5:])
        else:
            current_dir.size += int(line.split()[0])
    print_sum_of_big_dir(system)
    print_smallest_dir_to_delete(system)


def print_sum_of_big_dir(system: list[Directory]):
    sum_of_big_dir = sum(filter(lambda size: size < 100000, map(lambda directory: directory.get_full_size(), system)))
    print('Sum of the total sizes of directories with a total size of at most 100000 :', sum_of_big_dir)


def print_smallest_dir_to_delete(system: list[Directory]):
    unused_space = SYSTEM_SIZE - system[0].get_full_size()
    smallest_dir = sorted(filter(lambda size: (unused_space + size) >= UPDATE_SIZE,
                                 map(lambda directory: directory.get_full_size(), system)))[0]
    print('Size of the smallest directory to delete to free up enough space to run the update :', smallest_dir)
