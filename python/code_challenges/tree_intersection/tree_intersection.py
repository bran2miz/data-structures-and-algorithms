def tree_intersection(first_tree, second_tree):
    first_tree_set = set(first_tree.pre_order())
    intersection = first_tree_set.intersection(second_tree.pre_order())
    new_list = list(intersection)
    return new_list
