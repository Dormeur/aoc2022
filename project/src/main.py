from day1.elfCaloriesCalcul import *
from day2.rpsGameBuilder import *
from day3.rucksackBuilder import *
from day4.elfsPairBuilder import *


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
    build_elfs_pair_list()
    get_sum_of_assignment_fully_containing_other()
    get_sum_of_assignment_overlap_other()
    print('---Day 5---')


if __name__ == "__main__":
    all_day()
