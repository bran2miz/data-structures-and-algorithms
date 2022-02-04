from stacks_and_queue.pseudo_queue import PseudoQueue
import pytest

def test_pseudo_queue():
    pseudo = PseudoQueue()
    assert pseudo

def test_pseudo_queue_enqueue_one():
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue(3)
    actual = pseudo_queue.stack_1.peek()
    expected = 3
    assert actual == expected

def test_pseudo_queue_enqueue_two():
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue(1)
    pseudo_queue.enqueue(2)
    actual = pseudo_queue.stack_1.peek()
    expected = 2
    assert actual == expected

def test_pseudo_queue_enqueue_multi():
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue(1)
    pseudo_queue.enqueue(2)
    pseudo_queue.enqueue(3)

    actual = pseudo_queue.dequeue()
    expected = 1
    assert actual == expected

    actual = pseudo_queue.dequeue()
    expected = 2
    assert actual == expected

    actual = pseudo_queue.dequeue()
    expected = 3
    assert actual == expected

    with pytest.raises(Exception):
        actual = pseudo_queue.dequeue()

def test_pseudo_queue_enqueue_multi_two():
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue(1)
    pseudo_queue.enqueue(2)
    pseudo_queue.enqueue(3)

    actual = pseudo_queue.dequeue()
    expected = 1
    assert actual == expected

    pseudo_queue.enqueue(6)
    actual = pseudo_queue.dequeue()
    expected = 2
    assert actual == expected

    actual = pseudo_queue.dequeue()
    expected = 3
    assert actual == expected

    actual = pseudo_queue.dequeue()
    expected = 6

    with pytest.raises(Exception):
        actual = pseudo_queue.dequeue()

def test_pseudo_queue_is_empty():
    pseudo_queue= PseudoQueue()
    with pytest.raises(Exception):
        pseudo_queue.dequeue()

