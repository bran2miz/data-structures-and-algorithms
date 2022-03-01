from code_challenges.trees.trees.trees import KaryTree

def fizz_buzz(tree):
    if tree.root is None:
        return None

    kary_tree = KaryTree()
    def walk(root):
        if root is None:
            return None
        if root.value % 5 == 0 and root.value % 3 == 0:
            kary_tree.add('fizzbuzz')
        elif root.value % 3 == 0:
            kary_tree.add('fizz')
        elif root.value % 5 == 0:
            kary_tree.add('buzz')
        else:
            kary_tree.add(str(root.value))

    walk(tree.root)
    return kary_tree
