from code_challenges.trees.trees.trees import KaryTree

def fizz_buzz(tree):
    if tree.root is None:
        return None

    k = KaryTree()
    def walk(root):
        if root is None:
            return None
        if root.value % 5 == 0 and root.value % 3 == 0:
            k.add('fizzbuzz')
        elif root.value % 3 == 0:
            k.add('fizz')
        elif root.value % 5 == 0:
            k.add('buzz')
        else:
            k.add(str(root.value))

    walk(tree.root)
    return k
