from day1.elfCaloriesCalcul import *
from day2.rpsCalcul import *
from day3.rucksackBuilder import *


def all_day():
    print('---Day 1---')
    build_elf_list()
    get_max_elf_calories()
    get_total_of_3_max_elf_calories()
    print('---Day 2---')
    build_game_list()
    get_total_score()
    build_game_with_strat_list()
    get_total_score()
    print('---Day 3---')
    build_rucksacks_list()
    get_shared_item_priorities()
    build_elfs_group_list()
    get_badge_priorities()
    print('---Day 4---')


if __name__ == "__main__":
    all_day()
