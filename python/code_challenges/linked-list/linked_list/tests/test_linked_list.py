from linked_list.linked_list import Node, LinkedList
import pytest

def test_node_instance():
    node = Node(1, None)
    assert node.next == None
    assert node.value == 1

def test_node_instance_fail():
    node = Node(1, None)
    assert node.next != node
    assert node.value != 2

def test_linked_list():
    node = Node(1, None)
    ll = LinkedList(node)
    assert ll.head == node

def test_linked_list_empty():
    ll = LinkedList()
    assert ll.head == None

def test_insert_to_empty_linked_list():
    # ll.head = apple
    ll = LinkedList()
    ll.insert('apple')
    assert ll.head.value == 'apple'

def test_insert_list():
    test_out_list = LinkedList()
    test_out_list.insert(10)
    actual = test_out_list.head.value
    expected = 10
    assert actual == expected

def test_insert_to_string():
    test_out_insert_to_string = LinkedList()
    test_out_insert_to_string.insert('a')
    test_out_insert_to_string.insert('b')
    test_out_insert_to_string.insert('c')
    actual = test_out_insert_to_string.head.value
    expected = 'c'
    assert actual == expected
    actual = test_out_insert_to_string.to_string()
    expected = '{ c } -> { b } -> { a } -> NONE'
    assert actual == expected

def test_insert_to_string_with_true():
    test_insert_to_string_include_true = LinkedList()
    test_insert_to_string_include_true.insert('a')
    test_insert_to_string_include_true.insert('b')
    test_insert_to_string_include_true.insert('c')
    actual = test_insert_to_string_include_true.includes('b')
    expected = True
    assert actual == expected

def test_insert_to_string_with_false():
    test_insert_to_string_include_false = LinkedList()
    test_insert_to_string_include_false.insert('a')
    test_insert_to_string_include_false.insert('b')
    test_insert_to_string_include_false.insert('c')
    actual = test_insert_to_string_include_false.includes('z')
    expected = False
    assert actual == expected

def test_to_append():
    ll = LinkedList()
    ll.append(7)
    expected = 7
    actual = ll.head.value
    assert expected == actual

def test_to_append_multiple_items():
    ll = LinkedList(Node(10))
    ll.append(3)
    ll.append(4)
    actual = ll.to_string()
    expected = '{ 10 } -> { 3 } -> { 4 } -> NONE'
    assert actual == expected

def test_insert_before():
    ll = LinkedList(Node(10))
    ll.head.next = Node(7)
    ll.head.next.next = Node(2)
    ll.head.next.next.next = Node(5)
    ll.insert_before(2, 8)
    actual = ll.to_string()
    expected = '{ 10 } -> { 7 } -> { 8 } -> { 2 } -> { 5 } -> NONE'

def test_insert_before_first_node():
    ll = LinkedList(Node(10))
    ll.insert_before(10, 2)
    actual = ll.to_string()
    expected = '{ 2 } -> { 10 } -> NONE'
    assert actual == expected

def test_insert_before_alerts_exception():
    with pytest.raises(Exception):
        ll = LinkedList(Node(10))
        ll.head.next = Node(7)
        ll.head.next.next = Node(2)
        ll.head.next.next.next = Node(5)
        ll.insert_before(9, 1)

def test_insert_after():
    ll = LinkedList(Node(10))
    ll.head.next = Node(7)
    ll.head.next.next = Node(2)
    ll.head.next.next.next = Node(5)
    ll.insert_after(2, 14)
    actual = ll.to_string()
    expected = '{ 10 } -> { 7 } -> { 2 } -> { 14 } -> { 5 } -> NONE'
    assert actual == expected

def test_insert_after_final_node():
    ll = LinkedList(Node(10))
    ll.head.next = Node(7)
    ll.head.next.next = Node(2)
    ll.insert_after(2, 14)
    actual = ll.to_string()
    expected = '{ 10 } -> { 7 } -> { 2 } -> { 14 } -> NONE'
    assert actual == expected

def test_insert_after_alerts_exception():
    with pytest.raises(Exception):
        ll = LinkedList(Node(10))
        ll.head.next = Node(7)
        ll.head.next.next = Node(2)
        ll.head.next.next.next = Node(5)
        ll.insert_after(6, 13)

def test_insert_to_linked_list():
    # ll
    # node1
    # node2
    # ll.head = apple
    # apple.next = pear
    # pear.next = None

    # [apple] -> [pear] -> None

    ll = LinkedList()
    # head is none
    node1 = Node('apple')
    # ll.head is none
    ll.head == node1
    # ll.head is apple
    node2 = Node('pear')
    # apple.next is none
    node1.next = node2
    # apple.next is pear
    # [apple] -> [pear] -> None
    ll.insert('bananna')
    # [bananna] -> [apple] -> [pear]
    assert ll.head.value == 'bananna'

def test_includes_in_ll(ll):
    expected = True
    actual = ll.includes(3000)
    assert expected == actual


def test_includes_in_ll(ll):
    expected = False
    actual = ll.includes(400)
    assert expected == actual


@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(1)
    ll.insert('apple')
    ll.insert(1991)
    return ll
