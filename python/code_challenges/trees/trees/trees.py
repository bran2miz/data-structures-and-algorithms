from code_challenges.trees.trees.node import Node

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        # root > left > right
        #           A
        #       /       \
        #      B         C
        #   /    \     /
        #  D     E    F

        # Expect A B D E C F

        # empty list for values
        values = []

        def walk(root):
            if root is None:
                return
            if root:
                values.append(root.value)
                walk(root.left)
                walk(root.right)

        walk(self.root)
        return values

    def in_order(self):
        # left > root > right
        values = []

        if self.root == None:
            return

        def walk(node):
            if node:
                walk(node.left)
                values.append(node.value)
                walk(node.right)
        walk(self.root)
        return values

    def post_order(self):
        # left > right > root
        values = []

        if self.root == None:
            return

        def walk(node):
            if node:
                walk(node.left)
                walk(node.right)
                values.append(node.value)
        walk(self.root)
        return values

    def max_tree(self):

        if self.root == None:
            raise Exception('Sorry this Tree is currently empty')

        z = {'max_value': 0}

        def walk(node, z):
            if node:
                walk(node.left,z)
                walk(node.right,z)
                if node.value > z['max_value']:
                    z['max_value'] = node.value
        walk(self.root, z)
        return z['max_value']

class BinarySearchTree(BinaryTree):
    def add(self, value):
        def walk(root):
            if value < root.value:
                if root.left is None:
                    root.left = Node(value)
                else:
                    walk(root.left)
            else:
                if root.right is None:
                    root.right = Node(value)
                else:
                    walk(root.right)
        walk(self.root)

    def contains(self, value):
        def walk(root):
            if root is None:
                return False
            elif root.value == value:
                return True
            elif value < root.value:
                return walk(root.left)
            else:
                return walk(root.right)
        return walk(self.root)


class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def add(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node

        def walk(root, curr_node):
            if root is None:
                return

            if curr_node.value < root.value:
                if root.left:
                    walk(root.left, curr_node)
                else:
                    root.left = curr_node
            else:
                if root.right:
                    walk(root.right, curr_node)
                else:
                    root.right = curr_node
        walk(self.root, node)
