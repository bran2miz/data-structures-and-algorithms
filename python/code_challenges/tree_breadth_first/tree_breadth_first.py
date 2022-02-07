# from stack_and_queue.stacks_and_queue.queue import Queue
# from code_challenges.trees.trees.trees import BinaryTree
# from trees.trees import BinaryTree
# from trees.node import Node

def breadth_first(tree):
    queue_list = []
    values = []

    if tree.root:
        queue_list.insert(0, tree.root)

    while queue_list:
        node = queue_list.pop()
        values.append(node.value)
        if node.left:
            queue_list.insert(0, node.left)
        if node.right:
            queue_list.insert(0, node.right)

    return values
