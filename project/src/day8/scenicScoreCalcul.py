def look_at_tree_on_y_axis(forest, tree: int, y_range: range, x: int) -> int:
    number_of_tree = 0

    if y_range.start == y_range.stop:
        return number_of_tree

    for y in y_range:
        number_of_tree += 1
        if forest[y][x] >= tree:
            return number_of_tree

    return 1 if number_of_tree == 0 else number_of_tree


def look_at_tree_on_x_axis(forest, tree: int, y: int, x_range: range) -> int:
    number_of_tree = 0

    if x_range.start == x_range.stop:
        return number_of_tree

    for x in x_range:
        number_of_tree += 1
        if forest[y][x] >= tree:
            return number_of_tree

    return 1 if number_of_tree == 0 else number_of_tree


def count_visible_tree(forest, tree: int, y: int, x: int) -> int:
    top = look_at_tree_on_y_axis(forest, tree, range(y-1, -1, -1), x)
    bottom = look_at_tree_on_y_axis(forest, tree, range(y + 1, forest.__len__()), x)
    left = look_at_tree_on_x_axis(forest, tree, y, range(x-1, -1, -1))
    right = look_at_tree_on_x_axis(forest, tree, y, range(x + 1, forest.__len__()))
    return top * bottom * left * right
