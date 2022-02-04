
from trees.trees.trees import BinaryTree
from tree_breadth_first.tree_breadth_first import breadth_first
import pytest

@pytest.mark.skip("TODO")
def test_breadth_first():
    tree = BinaryTree()
    assert breadth_first(tree) == []

# # @pytest.mark.skip("TODO")
# def test_breadth_first_root():
#     one = Node(1)
#     tree = BinaryTree(one)
#     assert breadth_first(tree) == [1]
