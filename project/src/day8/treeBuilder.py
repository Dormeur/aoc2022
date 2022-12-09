import numpy as np

from day8.isTreeVisible import is_tree_visible
from day8.scenicScoreCalcul import count_visible_tree
from utils import read_file


def tree_builder():
    f = read_file('../resources/input_day_8.txt')
    forest = np.array([[int(tree) for tree in line] for line in f])
    it = np.nditer(forest, flags=['multi_index'])
    total_tree_visible: int = 0
    scenic_scores = []
    for tree in it:
        total_tree_visible += is_tree_visible(forest, tree, it.multi_index[0], it.multi_index[1])
        scenic_scores.append(count_visible_tree(forest, tree, it.multi_index[0], it.multi_index[1]))
    print(total_tree_visible)
    print(max(scenic_scores))
