from day1.elfBuilder import *
from day10.signalBuilder import *
from day2.rpsGameBuilder import *
from day3.rucksackBuilder import *
from day4.elfsPairBuilder import *
from day5.stackBuilder import *
from day6.markerBuilder import *
from day7.directoryBuilder import *
from day8.treeBuilder import *
from day9.ropeBuilder import *


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
    build_stack_and_move_list()
    start_crate_mover_9000()
    get_all_top_crate()
    build_stack_and_move_list()
    start_crate_mover_9001()
    get_all_top_crate()
    print('---Day 6---')
    build_start_of_packet_marker()
    build_start_of_message_marker()
    print('---Day 7---')
    build_directory()
    print('---Day 8---')
    tree_builder()
    print('---Day 9---')
    build_rope(1)
    build_rope(9)
    print('---Day 10---')
    build_signal()
    print_sum_of_monitored_cycles()
    print_screen()
    print('---Day 11---')

if __name__ == "__main__":
    # all_day()
