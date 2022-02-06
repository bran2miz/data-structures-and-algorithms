from code_challenges.trees.trees.node import Node
from code_challenges.trees.trees.trees import BinaryTree
from code_challenges.tree_breadth_first.tree_breadth_first import breadth_first
import pytest

# @pytest.mark.skip("TODO")
def test_breadth_first():
    tree = BinaryTree()
    assert breadth_first(tree) == []

def test_breadth_first_root():
    root = Node(1)
    tree = BinaryTree(root)
    assert breadth_first(tree) == [1]


def test_breadth_first_test_2():
    tree_traversal = (Node(5, Node(4, Node(1), Node(2)), Node(7, Node(8), Node(6)) ))
    tree = BinaryTree(tree_traversal)
    assert breadth_first(tree) == [5, 4, 7, 1, 2, 8, 6]


def test_breadth_first_example():
    tree = BinaryTree(Node(2))
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right = Node(5)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    assert breadth_first(tree) == [2,7,5,2,6,9,5,11,4]
