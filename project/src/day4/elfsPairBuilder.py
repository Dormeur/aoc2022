from typing import List

from day4.elfsPair import ElfsPair
from utils import read_file

elfsPairs: List[ElfsPair] = []


def build_section(line) -> List[int]:
    section = []
    start = int(line[0])
    end = int(line[1]) + 1
    for i in range(start, end):
        section.append(i)
    return section


def build_elfs_pair_list():
    f = read_file("../ressources/input_day_4.txt")
    for line in f:
        elfs_section_number = line.split(',')
        first_elf_section = build_section(elfs_section_number[0].split('-'))
        second_elf_section = build_section(elfs_section_number[1].split('-'))
        elfsPairs.append(ElfsPair(first_elf_section, second_elf_section))


def get_sum_of_assignment_fully_containing_other():
    print(sum(elfsPair.is_section_fully_containing_other() for elfsPair in elfsPairs))


def get_sum_of_assignment_overlap_other():
    print(sum(elfsPair.is_section_overlaps_other() for elfsPair in elfsPairs))
