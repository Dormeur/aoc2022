def look_at_tree_on_y_axis(forest, tree: int, y_range: range, x: int) -> int:
    for y in y_range:
        if forest[y][x] >= tree:
            return False
    return True


def look_at_tree_on_x_axis(forest, tree: int, y: int, x_range: range) -> int:
    for x in x_range:
        if forest[y][x] >= tree:
            return False
    return True


def is_tree_visible(forest, tree: int, y: int, x: int) -> int:
    if look_at_tree_on_y_axis(forest, tree, range(y-1, -1, -1), x):
        return 1
    elif look_at_tree_on_y_axis(forest, tree, range(y + 1, forest.__len__()), x):
        return 1
    elif look_at_tree_on_x_axis(forest, tree, y, range(x-1, -1, -1)):
        return 1
    elif look_at_tree_on_x_axis(forest, tree, y, range(x + 1, forest.__len__())):
        return 1
    else:
        return 0
