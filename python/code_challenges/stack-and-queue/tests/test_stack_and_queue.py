from stacks_and_queue.node import Node
from stacks_and_queue.queue import Queue
from stacks_and_queue.stack import Stack
import pytest

def test_stack_top_is_none():
    stack = Stack()
    assert stack.top == None

def test_stack_push():
    stack = Stack()
    stack.push(3)
    actual = stack.top.value
    expected = 3
    assert actual == expected

def test_stack_multiple_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    actual = stack.top.value
    expected = 3
    assert actual == expected

def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.pop()
    assert stack.top == None

def test_stack_multiple_pops():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.pop()
    expected = Exception
    assert actual == expected

# @pytest.mark.skip(reason = 'pending')
def test_two_stack_pop():
    stack = Stack()
    actual = stack.pop()
    expected = Exception
    assert actual == expected

def test_three_stack_pop():
    stack = Stack()
    stack.push('hello')
    actual = stack.pop()
    expected = 'hello'
    assert actual == expected

def test_stack_peek():
    stack = Stack()
    stack.push(3)
    actual = stack.peek()
    expected = 3
    assert actual == expected

def test_stack_is_empty():
    stack = Stack()
    actual = stack.isEmpty()
    expected = True
    assert actual == expected

def test_stack_two_is_empty():
    stack = Stack()
    stack.push('hello')
    actual = stack.isEmpty()
    expected = False
    assert actual == expected

def test_queue_enqueue():
    queue = Queue()
    actual = queue.front
    expected= None
    assert actual == expected

def test_queue_two_enqueue():
    queue = Queue()
    queue.enqueue(3)
    actual = queue.peek()
    expected = 3
    assert actual == expected

def test_queue_three_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual = queue.peek()
    expected = 1
    assert actual == expected

def test_queue_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)

    queue.dequeue()
    actual = queue.peek()
    expected = 2
    assert actual == expected

def test_queue_multi_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    # dequeue removes all front items until the rear is set as the front
    queue.dequeue()
    actual = queue.peek()
    expected = 4
    assert actual == expected

def test_queue_is_empty():
    queue = Queue()
    actual = queue.isEmpty()
    expected = True
    assert actual == expected

def test_queue_empty_queue():
    with pytest.raises(Exception):
        queue = Queue()
        queue.peek()

