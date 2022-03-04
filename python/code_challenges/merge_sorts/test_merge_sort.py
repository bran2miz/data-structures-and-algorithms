from merge_sort import merge_sort

def test_import():
    assert merge_sort

def test_merge_sort():
    array = [8,4,23,42,16,15]
    merge_sort(array)
    assert array == [4,8,15,16,23,42]

def test_merge_sort_two():
    array = [20,18,12,8,5,-2]
    merge_sort(array)
    assert array == [-2,5,8,12,18,20]

def test_merge_sort_three():
    array = [5,12,7,5,5,7]
    merge_sort(array)
    assert array == [5,5,5,7,7,12]

def test_merge_sort_four():
    array = [2,3,5,7,13,11]
    merge_sort(array)
    assert array == [2,3,5,7,11,13]
