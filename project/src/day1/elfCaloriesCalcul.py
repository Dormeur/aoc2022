import functools

from day1.elf import Elf

elfs = [Elf()]


def build_elf_list():
    current_elf_index = 0
    f = open("../ressources/input_day_1.txt", "r")
    for line in f:
        if line.rstrip().isdigit():
            elfs[current_elf_index].calories += int(line)
        else:
            current_elf_index += 1
            elfs.append(Elf())


def get_max_elf_calories():
    print(functools.reduce(lambda a, b: a if a.calorie > b.calorie else b, elfs).calories)


def get_total_of_3_max_elf_calories():
    elfs.sort(key=lambda e: e.calories, reverse=True)
    print(sum(elf.calories for elf in elfs[:3]))
