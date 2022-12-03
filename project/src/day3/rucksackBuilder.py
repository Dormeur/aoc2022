from day3.charToInt import char_to_int
from day3.elfsGroup import ElfsGroup
from day3.rucksack import Rucksack

rucksacks = []
elfsGroups = []


def build_rucksacks_list():
    f = open("../ressources/input_day_3.txt", "r")
    for line in f:
        rucksacks.append(Rucksack(line.rstrip()))


def get_shared_item_priorities():
    print(sum(char_to_int(rucksack.get_shared_item()) for rucksack in rucksacks))


def build_elfs_group_list():
    rucksacks.clear()
    build_rucksacks_list()
    i = 0
    while i < rucksacks.__len__():
        elfsGroups.append(ElfsGroup([rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]]))
        i += 3


def get_badge_priorities():
    print(sum(char_to_int(group.get_badge()) for group in elfsGroups))
