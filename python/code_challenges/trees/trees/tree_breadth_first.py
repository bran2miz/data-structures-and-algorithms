from code_challenges.stack_and_queue.stacks_and_queue.queue import Queue

def breadth_first(tree):
    list = []
    breadth = Queue()
    if tree.root is None:
        return list
    breadth.enqueue(tree.root)
    while not breadth.isEmpty():
        front = breadth.dequeue()
        list.append(front.value)
        if front.left:
            breadth.enqueue(front.left)
        if front.right:
            breadth.enqueue(front.right)
    return list
