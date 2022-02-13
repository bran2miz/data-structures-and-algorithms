from code_challenges.trees.trees.trees import KaryTree
from code_challenges.tree_fizz_buzz.tree_fizz_buzz import fizz_buzz

def test_kary_tree():
    assert KaryTree()

def test_fizz_buzz():
    assert fizz_buzz

def test_kary_tree_fizz_buzz():
    kt = KaryTree()
    kt.add(1)
    assert kt.root.value == 1

def test_kary_tree_fizz_buzz_fizz():
    kt = KaryTree()
    kt.add(3)
    assert fizz_buzz(kt).root.value == 'fizz'


def test_tree_fizz_buzz_add_divisible_3():
    kt = KaryTree()
    kt.add(12)
    assert fizz_buzz(kt).root.value == 'fizz'

def test_k_fizz_buzz_buzz_divisible_5():
    kt = KaryTree()
    kt.add(10)
    assert fizz_buzz(kt).root.value == 'buzz'


def test_k_fizz_buzz_fizz_buzz():
    kt = KaryTree()
    kt.add(30)
    assert fizz_buzz(kt).root.value == 'fizzbuzz'

def test_k_fizz_buzz_fizz_both():
    kt = KaryTree()
    kt.add(60)
    assert fizz_buzz(kt).root.value == 'fizzbuzz'

def test_k_fizz_buzz_fizzbuzz():
    kt = KaryTree()
    kt.add(45)
    assert fizz_buzz(kt).root.value == 'fizzbuzz'

def test_k_fizz_buzz_not_fizzbuzz():
    kt = KaryTree()
    kt.add(16)
    assert fizz_buzz(kt).root.value != 'fizzbuzz'
