from tree_intersection import tree_intersection
from code_challenges.trees.trees.node import Node
from code_challenges.trees.trees.trees import BinaryTree

def test_import():
    assert tree_intersection

def test_tree_intersection():

    tree = Node(150)
    tree.left = Node(100)
    tree.right = Node(250)
    tree.left.left = Node(75)
    tree.left.right = Node(160)
    tree.right.left = Node(200)
    tree.right.right = Node(600)


    tree_two = Node(42)
    tree_two.left = Node(100)
    tree_two.right = Node(600)
    tree_two.left.left = Node(15)
    tree_two.left.right = Node(160)
    tree_two.right.left = Node(200)
    tree_two.right.right = Node(350)

    first_tree = BinaryTree(tree)
    second_tree = BinaryTree(tree_two)

    assert tree_intersection(first_tree, second_tree) == [160, 600, 100, 200]

def test_tree_intersection_2():

    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(6)
    tree.left.right = Node(5)

    tree_two = Node(1)
    tree_two.left = Node(2)
    tree_two.right = Node(3)
    tree_two.left.left = Node(4)
    tree_two.left.right = Node(7)

    first_tree = BinaryTree(tree)
    second_tree = BinaryTree(tree_two)

    assert tree_intersection(first_tree, second_tree) == [1,2,3]

def test_tree_intersection_3():

    one = Node(15)
    one.left = Node(312)
    one.right = Node(47)
    one.left.right = Node(190)

    two = Node(15)
    two.left = Node(600)
    two.right = Node(47)
    two.left.left = Node(789)

    tree_1 = BinaryTree(one)
    tree_2 = BinaryTree(two)

    assert tree_intersection(tree_1,tree_2) == [47, 15]
